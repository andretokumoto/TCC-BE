def open_template(template_path):
    with open(template_path, 'r') as template_file:
        template = template_file.read()  
    return template

def salva_arquivo(output_path, doc_gerado):
    with open(output_path, 'w') as output_file:
        output_file.write(doc_gerado)  

def to_pdf(dados):
    ...

def to_tex(dados):

    document_type = dados.get('document_type')
    output_path = 'FormataiBE_API/templates/arquivo_gerado.tex'
    
    if document_type == 'oficio':

        template_path = 'FormataiBE_API/templates/oficio.tex'
        template = open_template(template_path)
        
        doc_gerado = template.replace('__OFICIO_NUMERO__', dados.get('oficio_numero', ''))
        doc_gerado = doc_gerado.replace('__DESTINATARIO__', dados.get('destinatario', ''))
        doc_gerado = doc_gerado.replace('__ENDERECO_DESTINATARIO__', dados.get('endereco_destinatario', ''))
        doc_gerado = doc_gerado.replace('__CIDADE_ESTADO__', dados.get('cidadeEstado_destinatario', ''))
        doc_gerado = doc_gerado.replace('__CEP__', dados.get('cep_destinatario', ''))
        doc_gerado = doc_gerado.replace('__TEXTO_SOLICITACAO__', dados.get('corpo_mensagem', ''))
        doc_gerado = doc_gerado.replace('__NOME_REMETENTE__', dados.get('nome_remetente', ''))
        doc_gerado = doc_gerado.replace('__CARGO_REMETENTE__', dados.get('cargo_remetente', ''))
        doc_gerado = doc_gerado.replace('__ORGANIZACAO_REMETENTE__', dados.get('organizacao_remetente', ''))
        
        salva_arquivo(output_path, doc_gerado)

    elif document_type == 'memorando':

        template_path = 'FormataiBE_API/templates/memorando.tex'
        template = open_template(template_path)
        
        doc_gerado = template.replace('__DESTINATARIO__', dados.get('destinatario', ''))
        doc_gerado = doc_gerado.replace('__CORPO__', dados.get('corpo_mensagem', ''))
        doc_gerado = doc_gerado.replace('__ASSUNTO__', dados.get('assunto', ''))
        doc_gerado = doc_gerado.replace('__NOME_REMETENTE__', dados.get('nome_remetente', ''))
        doc_gerado = doc_gerado.replace('__CARGO_REMETENTE__', dados.get('cargo_remetente', ''))
        doc_gerado = doc_gerado.replace('__ORGANIZACAO_REMETENTE__', dados.get('organizacao_remetente', ''))
        
        salva_arquivo(output_path, doc_gerado)

    return output_path


