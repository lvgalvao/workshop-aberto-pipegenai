from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, validator, ValidationError
from datetime import datetime, time
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "ZapFlow com Gemini"
    produto2 = "ZapFlow com chatGPT"
    produto3 = "ZapFlow com Llama3.0"

class Vendas(BaseModel):
    """
    Modelo de dados para as vendas.

    Args:
        email (str): email do comprador
        data (datetime): data da compra
        valor (int): valor da compra
        produto (str): nome do produto
        quantidade (int): quantidade de produtos
        produto (str): categoria do produto
    """
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum

    @validator('data')
    def validar_intervalo_data(cls, v):
        # Define o intervalo de horas permitido no mesmo dia (ex: das 9h às 17h)
        inicio_intervalo = datetime.combine(v.date(), time(9, 0))  # 09:00
        fim_intervalo = datetime.combine(v.date(), time(17, 0))    # 17:00

        # Verifica se a data está dentro do intervalo permitido
        if not (inicio_intervalo <= v <= fim_intervalo):
            raise ValueError("A data deve estar dentro do intervalo de 09:00 às 17:00 no mesmo dia.")
        return v

    @validator('produto')
    def categoria_deve_estar_no_enum(cls, v):
        return v
