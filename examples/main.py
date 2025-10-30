import pandas as pd

name_column = [f'column_{i}' for i in range(14) ]

df_excell = pd.read_excel('cotacao-compra.xlsx', header=None, names=name_column)
# print(df_excell.loc[12, 'column_5'])

# # Cabeçalho da lista de Itens do Pedido
head_list = 6 # Tras o tilulo da lista de itens da planiha de pedidos
description = df_excell.iloc[head_list,0] #: str = Field(..., description="Descrição do item do pedido")
quantity = df_excell.iloc[head_list,2] #: Decimal = Field(..., gt=0, description="Quantidade do item, deve ser > 0")
unit = df_excell.iloc[head_list,3] #: str = Field(..., description="Unidade de medida, ex: 'kg', 'un'")
unit_price = df_excell.iloc[head_list,4] #: Decimal = Field(..., ge=0, description="Preço unitário do item, >= 0")
total_price = df_excell.iloc[head_list,5] #: Decimal = Field(..., ge=0, description="Valor total do item, calculado")
delivery_days = df_excell.iloc[head_list,6] #: int = Field(..., ge=0, description="Prazo em dias para entrega do item")
delivery_date = df_excell.iloc[head_list,7] #: date = Field(..., description="Data prevista de entrega")
ipi_percentage = df_excell.iloc[head_list,8] #: Decimal = Field(..., ge=0, description="Percentual de IPI aplicado")
ipi_value = "IPI Valor" #: Decimal = Field(..., ge=0, description="Valor do IPI aplicado")
icms_percentage = df_excell.iloc[head_list,9] #: Decimal = Field(..., ge=0, description="Percentual de ICMS aplicado")
icms_value = "ICMS Valor" #: Decimal = Field(..., ge=0, description="Valor do ICMS aplicado")
freight_value = df_excell.iloc[head_list,10] #: Decimal = Field(..., ge=0, description="Valor do frete do item")
note = df_excell.iloc[head_list,11] #: Optional[str] = Field(None, description="Observação opcional do item")

print('|',description,'|', quantity,'|', unit,'|', unit_price,'|', total_price,'|', delivery_days,'|', delivery_date,'|', ipi_percentage,'|', ipi_value, '|', icms_percentage,'|', icms_value,'|', freight_value,'|', note, '|')


# Titulo dos campos principais
document_number = df_excell.loc[0,'column_0'] #: str = Field(..., description="Número do documento do pedido")
supplier_name = df_excell.loc[1,'column_0'] #: str = Field(..., description="Nome do fornecedor")
supplier_cnpj = df_excell.loc[2,'column_0'] #: str = Field(..., description="CNPJ do fornecedor")
supplier_id = "Cod. Fornecedor" #: int = Field(..., description="ID do fornecedor")
quotation_date = df_excell.loc[3,'column_0'] #: date = Field(..., description="Data de cotação do pedido")
delivery_date = df_excell.loc[4,'column_0'] #: date = Field(..., description="Data de entrega do pedido")
payment_condition = df_excell.loc[5,'column_0'] #: Optional[str] = Field(None, description="Condição de pagamento aplicada ao pedido")
total_items = df_excell.loc[12,'column_5'] #: Decimal = Field(..., ge=0, description="Total de itens do pedido")
total_freight = df_excell.loc[12,'column_10'] #: Decimal = Field(..., ge=0, description="Total do frete do pedido")
total_taxes = df_excell.loc[12,'column_11'] #: Decimal = Field(..., ge=0, description="Total de impostos do pedido")
total_order = "Total Geral"#: Decimal = Field(..., ge=0, description="Total geral do pedido (itens + frete + impostos)")

print('|', document_number, '|',supplier_name, '|',supplier_cnpj, '|',supplier_id, '|',quotation_date, '|',delivery_date,'|',payment_condition,'|',total_items, '|',total_freight, '|',total_taxes, '|',total_order, '|')