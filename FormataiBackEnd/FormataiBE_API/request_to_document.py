import subprocess
import os
import uuid

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'FormataiBE_API/templates')
TEMP_DIR = os.path.join(BASE_DIR, 'FormataiBE_API/templates/arquivos_temp')

# Garantir que o diretório temporário existe
os.makedirs(TEMP_DIR, exist_ok=True)

def open_template(template_path):
    with open(template_path, 'r', encoding='utf-8') as template_file:
        return template_file.read()

def salva_arquivo(output_path, doc_gerado):
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(doc_gerado)

def to_pdf(dados):
    """
    Gera o arquivo PDF usando o arquivo LaTeX criado.
    """
    tex_path = to_tex(dados)
    output_dir = os.path.dirname(tex_path)
    pdf_filename = os.path.basename(tex_path).replace('.tex', '.pdf')
    pdf_path = os.path.join(output_dir, pdf_filename)

    try:
        # Executa o comando pdflatex
        result = subprocess.run(
            ['pdflatex', '-output-directory', output_dir, tex_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Log do stdout para diagnóstico
        print(result.stdout.decode())

    except subprocess.CalledProcessError as e:
        # Log detalhado do erro
        error_message = f"Erro ao gerar PDF: {str(e)}\n{e.stderr.decode()}"
        print(error_message)
        raise RuntimeError(error_message)

    if not os.path.exists(pdf_path):
        raise FileNotFoundError("O arquivo PDF não foi gerado corretamente.")

    return pdf_path

def to_tex(dados):
    """
    Gera o arquivo LaTeX baseado nos dados fornecidos.
    """
    document_type = dados.get('document_type')
    output_path = os.path.join(TEMP_DIR, f"{uuid.uuid4().hex}.tex")

    if document_type == 'oficio':
        template_path = os.path.join(TEMPLATE_DIR, 'oficio.tex')
        template = open_template(template_path)

        doc_gerado = template.replace('__OFICIO_NUMERO__', dados.get('oficio_numero', ''))
        doc_gerado = doc_gerado.replace('__DESTINATARIO__', dados.get('destinatario', ''))
        doc_gerado = doc_gerado.replace('__ENDERECO_DESTINATARIO__', dados.get('endereco_destinatario', ''))
        doc_gerado = doc_gerado.replace('__CIDADE_ESTADO__', dados.get('cidadeEstado_destinatario', ''))
        doc_gerado = doc_gerado.replace('__CEP__', dados.get('cep_destinatario', ''))
        doc_gerado = doc_gerado.replace('__TEXTO_SOLICITACAO__', dados.get('corpo_mensagem', ''))
        doc_gerado = doc_gerado.replace('__ASSUNTO__', dados.get('assunto', ''))
        doc_gerado = doc_gerado.replace('__NOME_REMETENTE__', dados.get('nome_remetente', ''))
        doc_gerado = doc_gerado.replace('__CARGO_REMETENTE__', dados.get('cargo_remetente', ''))
        doc_gerado = doc_gerado.replace('__ORGANIZACAO_REMETENTE__', dados.get('organizacao_remetente', ''))

    elif document_type == 'memorando':
        template_path = os.path.join(TEMPLATE_DIR, 'memorando.tex')
        template = open_template(template_path)

        doc_gerado = template.replace('__DESTINATARIO__', dados.get('destinatario', ''))
        doc_gerado = doc_gerado.replace('__CORPO__', dados.get('corpo_mensagem', ''))
        doc_gerado = doc_gerado.replace('__ASSUNTO__', dados.get('assunto', ''))
        doc_gerado = doc_gerado.replace('__NOME_REMETENTE__', dados.get('nome_remetente', ''))
        doc_gerado = doc_gerado.replace('__CARGO_REMETENTE__', dados.get('cargo_remetente', ''))
        doc_gerado = doc_gerado.replace('__ORGANIZACAO_REMETENTE__', dados.get('organizacao_remetente', ''))

    else:
        raise ValueError("Tipo de documento inválido ou não suportado.")

    salva_arquivo(output_path, doc_gerado)
    return output_path
