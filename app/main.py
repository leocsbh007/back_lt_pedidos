from fastapi import FastAPI
from app.schemas import OrderBase,OrderIn, SupplierBase, SupplierIn


app = FastAPI(title='API LT Pedidos', description='API para importar e criar PDFs de arquivos em EXCELL', version="1.0.0")

orders = []
suppliers = []

@app.get('/')
def root():
    return{
        'status': 'ok'
    }


@app.get('/info')
def info():
    return{
        'title': app.title,
        'decription': app.description,
        'version': app.version
    }

@app.post('/order')
def create_new_order(order: OrderIn):    
    new_order = OrderBase(**order.model_dump()) # Recebendo dados no request body da requisição    
    orders.append(new_order)
    return{
        'message': 'Pedido adicionado com sucesso!'
    }

@app.get('/order')
def get_all_orders() -> list[OrderBase] | dict:    
    print(orders, end=" ")
    if not orders:
        return {
            'message': 'Ainda não existem Pedidos Cadastrados'
        }        
    return orders

@app.post('/supplier')
def create_new_supplier(supplier: SupplierIn):
    new_supplier = SupplierBase(**supplier.model_dump())
    suppliers.append(new_supplier)
    return{
        'message': 'Fornecedor adicionado com sucesso!'
    }

@app.get('/supplier')
def get_all_suppliers() -> list[SupplierIn] | dict:
    if len(suppliers) == 0:
        return{
            'message': 'Ainda não existem Fornecedores Cadastrados'
        }
    return orders