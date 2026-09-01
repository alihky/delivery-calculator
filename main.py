from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from typing import Optional, Literal
from pydantic import BaseModel, Field

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class DeliveryCalculation(BaseModel):
    month: int = Field(...,ge=1, le=12)                       # الشهر (رقم من 1 إلى 12)
    total_income: float = Field(..., ge=0)             # إجمالي المدخول
    tax_rate: Literal[5, 15] = Field(...)
    ateco_code: Literal['1', '2'] = Field(...)                   # كود الأتيكو (لتحديد نسبة الـ INPS لاحقاً)
    car_expenses_per_day: float= Field(..., ge=0)            # مصاريف السيارة الشهرية
    how_many_days_worked_this_month: int = Field(..., ge=0, le=31)
    car_insurance: Optional[float] = None  # تأمين السيارة السنوي (اختياري)

@app.get("/", response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/calculation")
async def calculation_net_income(data: DeliveryCalculation):


# خصم قيمة الضريبة
        percent_without_cost = 0.67
        income = data.total_income * percent_without_cost
        tax_amount = income * (data.tax_rate / 100)


# خصم قيمة الانبس الضمان الاجتماعي

        if data.ateco_code == '1':
            inps = income * (26.07 / 100)

        elif data.ateco_code == '2':
            inps = 243.75 # القيمة الثابتة الشهرية (2925 سنوية مقسومة على 12)

        else:
            inps = 0.0
# تامين السيارة
        monthly_car_insurance = (data.car_insurance / 12) if data.car_insurance else 0

# مصاريف السيارة الشهرية

        car_expenses = data.how_many_days_worked_this_month * data.car_expenses_per_day

# صافي الربح

        Total_expenses = (tax_amount + inps + car_expenses
                          + monthly_car_insurance)
        Net_income = data.total_income - Total_expenses
# ارجاع النتائج

        return {
            "total_income": data.total_income,
            "tax_amount": round(tax_amount, 2),
            "inps_amount": round(inps, 2),
            "car_expenses": round(car_expenses, 2),
            "total_expenses": round(Total_expenses, 2),
            "net_income": round(Net_income, 2)
        }





