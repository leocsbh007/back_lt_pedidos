from uuid import UUID, uuid4
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import date, datetime, timezone
from decimal import Decimal

# ------------------------------
# Supplier Schemas
# ------------------------------
class SupplierBase(BaseModel):
    id_supplier: UUID = Field(default_factory=uuid4, description="ID do Fornecedor")
    name: str = Field(..., description="Nome do Fornecedor")
    cnpj: str = Field(..., description="CNPJ do Fornecedor")
    email: Optional[EmailStr] = Field(None, description="Email do Fornecedor")
    phone: Optional[str] = Field(None, description="Telefone do Fornecedor")
    address: Optional[str] = Field(None, description="Endereço do Fornecedor")
    payment_condition: Optional[str] = Field(None, description="Condição de pagamento padrão do fornecedor")

class SupplierIn(SupplierBase):
    pass

class SupplierOut(SupplierBase):
    id_supplier: UUID = Field(default_factory=uuid4, description="ID do Fornecedor")
    creation_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc),
                                    description="Data da Criação do Registro")

    model_config = {
        "from_attributes": True
    }


# ------------------------------
# Order Item Schemas
# ------------------------------
class OrderItemBase(BaseModel):
    description: str = Field(..., description="Descrição do item do pedido")
    quantity: Decimal = Field(..., gt=0, description="Quantidade do item, deve ser > 0")
    unit: str = Field(..., description="Unidade de medida, ex: 'kg', 'un'")
    unit_price: Decimal = Field(..., ge=0, description="Preço unitário do item, >= 0")
    total_price: Decimal = Field(..., ge=0, description="Valor total do item, calculado")
    delivery_days: int = Field(..., ge=0, description="Prazo em dias para entrega do item")
    delivery_date: date = Field(..., description="Data prevista de entrega")
    ipi_percentage: Decimal = Field(..., ge=0, description="Percentual de IPI aplicado")
    ipi_value: Decimal = Field(..., ge=0, description="Valor do IPI aplicado")
    icms_percentage: Decimal = Field(..., ge=0, description="Percentual de ICMS aplicado")
    icms_value: Decimal = Field(..., ge=0, description="Valor do ICMS aplicado")
    freight_value: Decimal = Field(..., ge=0, description="Valor do frete do item")
    note: Optional[str] = Field(None, description="Observação opcional do item")

class OrderItemIn(OrderItemBase):
    pass

class OrderItemOut(OrderItemBase):
    id_item: int = Field(..., description="ID do Item")
    order_id: int = Field(..., description="ID do Pedido pai")
    creation_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc),
                                    description="Data de Criação do Registro")

    model_config = {
        "from_attributes": True
    }


# ------------------------------
# Order Schemas
# ------------------------------
class OrderBase(BaseModel):
    document_number: str = Field(..., description="Número do documento do pedido")
    supplier_name: str = Field(..., description="Nome do fornecedor")
    supplier_cnpj: str = Field(..., description="CNPJ do fornecedor")
    supplier_id: int = Field(..., description="ID do fornecedor")
    quotation_date: date = Field(..., description="Data de cotação do pedido")
    delivery_date: date = Field(..., description="Data de entrega do pedido")
    payment_condition: Optional[str] = Field(None, description="Condição de pagamento aplicada ao pedido")
    total_items: Decimal = Field(..., ge=0, description="Total de itens do pedido")
    total_freight: Decimal = Field(..., ge=0, description="Total do frete do pedido")
    total_taxes: Decimal = Field(..., ge=0, description="Total de impostos do pedido")
    total_order: Decimal = Field(..., ge=0, description="Total geral do pedido (itens + frete + impostos)")

class OrderIn(OrderBase):
    items: List[OrderItemIn] = Field(default_factory=list, description="Lista dos itens do Pedido")

class OrderOut(OrderBase):
    id_order: int = Field(..., description="ID do pedido")
    creation_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc),
                                    description="Data de criação do registro")
    items: List[OrderItemOut] = Field(default_factory=list, description="Lista dos itens do Pedido")

    model_config = {
        "from_attributes": True
    }
