import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
from datetime import datetime
import os

def excel_to_pdf_pandas(excel_path, pdf_path=None, sheet_name=None):
    """
    Converte arquivo Excel para PDF usando pandas e matplotlib.
    
    Parâmetros:
    excel_path (str): Caminho do arquivo Excel
    pdf_path (str): Caminho de saída do PDF (opcional)
    sheet_name (str/lista): Nome(s) da(s) planilha(s) para converter
    """
    
    # Verifica se o arquivo existe
    if not os.path.exists(excel_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {excel_path}")
    
    # Define o caminho do PDF se não for fornecido
    if pdf_path is None:
        pdf_path = os.path.splitext(excel_path)[0] + ".pdf"
    
    # Lê o arquivo Excel
    try:
        if sheet_name is None:
            # Lê todas as planilhas
            excel_file = pd.ExcelFile(excel_path)
            sheets = excel_file.sheet_names
        else:
            # Converte para lista se for string única
            sheets = [sheet_name] if isinstance(sheet_name, str) else sheet_name
        
        # Cria o PDF
        with PdfPages(pdf_path) as pdf:
            for sheet in sheets:
                # Lê a planilha
                df = pd.read_excel(excel_path, sheet_name=sheet, header=None)
                
                # Cria a figura
                fig, ax = plt.subplots(figsize=(11, 8.5))  # Tamanho A4
                ax.axis('tight')
                ax.axis('off')
                
                # Cria a tabela
                table = ax.table(
                    cellText=df.values,
                    colLabels=df.columns,
                    cellLoc='left',
                    loc='center',
                    bbox=[0, 0, 1, 1]
                )
                
                # Ajusta o tamanho da fonte
                table.auto_set_font_size(False)
                table.set_fontsize(8)
                
                # Ajusta a largura das células
                table.scale(1, 1.2)
                
                # Adiciona título da planilha
                ax.set_title(f'Planilha: {sheet}', fontsize=14, pad=20)
                
                # Ajusta layout
                plt.tight_layout()
                
                # Adiciona ao PDF
                pdf.savefig(fig, bbox_inches='tight')
                plt.close()
                
        print(f"Arquivo convertido com sucesso: {pdf_path}")
        
    except Exception as e:
        print(f"Erro na conversão: {str(e)}")
        return False
    
    return True

# Versão mais avançada com melhor formatação
def excel_to_pdf_advanced(excel_path, pdf_path=None, sheet_name=None):
    """
    Versão mais avançada com melhor formatação.
    """
    
    if not os.path.exists(excel_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {excel_path}")
    
    if pdf_path is None:
        pdf_path = os.path.splitext(excel_path)[0] + ".pdf"
    
    try:
        # Lê o arquivo Excel
        excel_file = pd.ExcelFile(excel_path)
        
        if sheet_name is None:
            sheets = excel_file.sheet_names
        else:
            sheets = [sheet_name] if isinstance(sheet_name, str) else sheet_name
        
        with PdfPages(pdf_path) as pdf:
            for sheet in sheets:
                # Lê a planilha mantendo valores originais
                df = pd.read_excel(excel_path, sheet_name=sheet, header=None, dtype=str)
                
                # Substitui NaN por string vazia
                df = df.fillna('')
                
                # Calcula tamanho da figura baseado no número de linhas/colunas
                nrows, ncols = df.shape
                fig_width = max(11, ncols * 0.5)  # Mínimo A4, ajusta pela largura
                fig_height = max(8.5, nrows * 0.3)  # Mínimo A4, ajusta pela altura
                
                fig, ax = plt.subplots(figsize=(fig_width, fig_height))
                ax.axis('off')
                
                # Cria tabela
                table = ax.table(
                    cellText=df.values,
                    colLabels=[f'Col {i+1}' for i in range(ncols)],
                    cellLoc='left',
                    loc='center'
                )
                
                # Formatação da tabela
                table.auto_set_font_size(False)
                table.set_fontsize(6)
                
                # Autoajuste das colunas
                table.auto_set_column_width([i for i in range(ncols)])
                
                # Título
                ax.set_title(f'{os.path.basename(excel_path)} - {sheet}', 
                           fontsize=12, pad=20, fontweight='bold')
                
                # Data no rodapé
                ax.text(0.5, -0.02, f'Gerado em: {datetime.now().strftime("%d/%m/%Y %H:%M")}', 
                       transform=ax.transAxes, ha='center', fontsize=8)
                
                pdf.savefig(fig, bbox_inches='tight')
                plt.close()
                
        print(f"PDF gerado com sucesso: {pdf_path}")
        
    except Exception as e:
        print(f"Erro: {str(e)}")
        return False
    
    return True

# Função para planilhas específicas com cabeçalho
def excel_to_pdf_with_header(excel_path, pdf_path=None, sheet_name=None, header_row=0):
    """
    Versão que usa a primeira linha como cabeçalho.
    """
    
    if not os.path.exists(excel_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {excel_path}")
    
    if pdf_path is None:
        pdf_path = os.path.splitext(excel_path)[0] + ".pdf"
    
    try:
        excel_file = pd.ExcelFile(excel_path)
        
        if sheet_name is None:
            sheets = excel_file.sheet_names
        else:
            sheets = [sheet_name] if isinstance(sheet_name, str) else sheet_name
        
        with PdfPages(pdf_path) as pdf:
            for sheet in sheets:
                # Lê com cabeçalho
                df = pd.read_excel(excel_path, sheet_name=sheet, header=header_row)
                df = df.fillna('')
                
                fig, ax = plt.subplots(figsize=(12, 8))
                ax.axis('off')
                
                table = ax.table(
                    cellText=df.values,
                    colLabels=df.columns,
                    cellLoc='left',
                    loc='center'
                )
                
                table.auto_set_font_size(False)
                table.set_fontsize(7)
                table.scale(1, 1.5)
                
                # Destaca cabeçalho
                for i in range(len(df.columns)):
                    table[(0, i)].set_facecolor('#f0f0f0')
                    table[(0, i)].set_text_props(weight='bold')
                
                ax.set_title(f'{sheet}', fontsize=14, pad=20)
                
                pdf.savefig(fig, bbox_inches='tight')
                plt.close()
                
        print(f"PDF gerado com sucesso: {pdf_path}")
        
    except Exception as e:
        print(f"Erro: {str(e)}")
        return False
    
    return True

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo básico
    excel_to_pdf_pandas('cotacao-compra.xlsx')
    
    # Exemplo avançado
    excel_to_pdf_advanced('cotacao-compra.xlsx', "output_avancado.pdf")
    
    # Exemplo com cabeçalho
    excel_to_pdf_with_header('cotacao-compra.xlsx', "output_com_header.pdf", header_row=0)