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
        # Define o intervalo de datas permitido
        inicio_intervalo = datetime(2024, 9, 1)  # 01/09/2024
        fim_intervalo = datetime(2024, 9, 12, 23, 59, 59)  # 12/09/2024 até 23:59:59

        # Verifica se a data está dentro do intervalo permitido
        if not (inicio_intervalo <= v <= fim_intervalo):
            raise ValueError("A data da venda deve estar entre 01/09/2024 e 12/09/2024.")
        return v

    @validator('produto')
    def categoria_deve_estar_no_enum(cls, v):
        return v
