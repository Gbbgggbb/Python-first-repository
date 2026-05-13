from flask import Flask

app = Flask(__name__)  # inicio o flask


@app.route(
    "/"
)  # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def curriculo():
    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo - Juninho Mayeutica dos Santos</title>
    <style>
        /* CSS Incorporado */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f4f4f9;
            margin: 0;
            padding: 20px;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #fff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }

        header {
            text-align: center;
            border-bottom: 2px solid #35424a;
            padding-bottom: 20px;
            margin-bottom: 20px;
        }

        h1 {
            margin: 0;
            color: #35424a;
            text-transform: uppercase;
        }

        .contato {
            color: #555;
            font-size: 0.9em;
        }

        h2 {
            color: #fff;
            background: #35424a;
            padding: 10px;
            border-radius: 4px;
            font-size: 1.2em;
        }

        .secao {
            margin-bottom: 20px;
        }

        .item-experiencia, .item-formacao {
            margin-bottom: 15px;
        }

        .cargo {
            font-weight: bold;
            color: #2c3e50;
        }

        .empresa-data {
            font-style: italic;
            color: #7f8c8d;
            display: flex;
            justify-content: space-between;
        }

        ul {
            padding-left: 20px;
        }

        @media (max-width: 600px) {
            .empresa-data {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>

<div class="container">
    <header>
        <h1>Juninho Mayeutica dos Santos</h1>
        <p class="contato">
            (11) 99999-9999 | juninho.mayeutica@email.com | São Paulo, SP<br>
            ://linkedin.com | ://github.com
        </p>
    </header>

    <section class="secao">
        <h2>Resumo Profissional</h2>
        <p>
            Profissional dedicado e analítico com sólida experiência em [Sua Área de Atuação, ex: Desenvolvimento Web/Administração]. Focado na resolução de problemas, melhoria de processos e aprendizado contínuo. Busco integrar uma equipe dinâmica para contribuir com resultados práticos e inovadores.
        </p>
    </section>

    <section class="secao">
        <h2>Experiência Profissional</h2>
        
        <div class="item-experiencia">
            <div class="cargo">Analista de Sistemas / Desenvolvedor</div>
            <div class="empresa-data">
                <span>Empresa Exemplo LTDA</span>
                <span>Janeiro 2021 - Presente</span>
            </div>
            <ul>
                <li>Desenvolvimento e manutenção de aplicações web utilizando HTML, CSS, JavaScript e React.</li>
                <li>Otimização de consultas SQL, resultando em melhora de 30% na performance do sistema.</li>
                <li>Implementação de metodologias ágeis (Scrum) para gestão de projetos.</li>
            </ul>
        </div>

        <div class="item-experiencia">
            <div class="cargo">Assistente Técnico</div>
            <div class="empresa-data">
                <span>Tecnologia S.A.</span>
                <span>Junho 2019 - Dezembro 2020</span>
            </div>
            <ul>
                <li>Suporte técnico a usuários internos e manutenção de infraestrutura de rede.</li>
                <li>Suporte na migração de servidores em nuvem (AWS).</li>
            </ul>
        </div>
    </section>

    <section class="secao">
        <h2>Formação Acadêmica</h2>
        <div class="item-formacao">
            <div class="cargo">Graduação em Análise e Desenvolvimento de Sistemas</div>
            <div class="empresa-data">
                <span>Universidade Exemplo (UniEx)</span>
                <span>Concluído em 2020</span>
            </div>
        </div>
    </section>

    <section class="secao">
        <h2>Habilidades</h2>
        <p><strong>Técnicas:</strong> HTML5, CSS3, JavaScript, SQL, Git, React, [Adicionar outras...].</p>
        <p><strong>Idiomas:</strong> Inglês Técnico (Leitura), Espanhol Básico.</p>
    </section>

</div>

</body>
</html>

"""  # Isso é o que será retornado quando a rota '/' for acessada


if __name__ == "__main__":
    app.run(
        debug=True
    )  # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento
