import json
from flask import Flask, request, jsonify

#app = Flask(__name__)

def gerar_tex(dados):
    #tamplete LaTeX de oficio
    template_oficio = fr"""
    \documentclass{{article}}
    \usepackage[utf8]{{inputenc}}
    \usepackage[brazil]{{babel}}
    \usepackage{{lipsum}} % Pacote para geração de texto de exemplo


    \usepackage[a4paper, margin=3cm]{{geometry}}

    \setlength{{\parskip}}{{1em}}

    \begin{{document}}

    \begin{{center}}
        \textbf{{OFÍCIO Nº {dados["oficio_numero"]}}}
    \end{{center}}

    \vspace{{1cm}}

    \begin{{flushright}}
        \textbf{{Destinatário}} \\
        {dados["destinatario"]} \\
        {dados["endereco_destinatario"]} \\
        {dados["cidade_estado"]} \\
        {dados["cep"]}
    \end{{flushright}}

    \vspace{{1cm}}

    \textbf{{Assunto:}} {dados["assunto"]}

    \vspace{{1cm}}

    Prezado(a) Senhor(a),

    \bigskip

    {dados["texto_solicitacao"]}

    \bigskip

    Atenciosamente,

    \vspace{{1cm}}

    \hrulefill \\
    {dados["nome_remetente"]} \\
    {dados["cargo_remetente"]} \\
    {dados["organizacao_remetente"]} \\

    \end{{document}}

    """
    with open('oficio.tex', 'w', encoding='utf-8') as tex_file:
        tex_file.write(template_oficio)
'''
@app.route('/receber-dados', methods=['POST'])
def receber_dados():
    if request.method == 'POST':
        dados = request.json  # Obtém os dados JSON do corpo da requisição
        #oficio_tex= gerar_tex(dados)

if __name__ == '__main__':
    app.run(debug=True)
'''

def main():
   
    dados_front = {
        "oficio_numero": "1234/2024",
        "destinatario": "GILDENORA BATISTA DANTAS MILHOMEM",
        "endereco_destinatario": "Subsecretária de Contabilidade Pública",
        "cidade_estado": "Secretaria do Tesouro Nacional",
        "cep": "Esplanada dos Ministérios Bloco P Anexo, Ala A, 1º Andar",
        "assunto": "Solicitação",
        "texto_solicitacao": """Eu, nome, estado civil, nacionalidade, profissão, portador do CPF número (informar) e de RG número (informar) residente à (endereço, com rua, número, bairro e complemento), CEP (informar), no município de (nome) – (estado), vem por meio deste comunicar o desligamento do funcionário (nome)
         a partir do dia (data de demissão do funcionário) Considera do que a solicitação será aprovada, fique com meus agradecimentos e votos de consideração.""",
        "nome_remetente": "Nome do Remetente",
        "cargo_remetente": "Cargo do Remetente",
        "organizacao_remetente": "Organização do Remetente"
    }

    
    gerar_tex(dados_front)


main()