# Amigo Fiel

Catálogo online de produtos para animais, desenvolvido em **Django** para a disciplina de Frameworks Back-End.

O backend segue os fundamentos do framework: model `ProdutoPet`, views de listagem (`ProdutoPet.objects.all()`) e detalhe (`ProdutoPet.objects.get(id=id)`), rota dinâmica, templates com `{% url %}` e `{% static %}`, Django Admin e arquivos estáticos. O frontend foi pensado como uma marca real de pet care, com design editorial, tipografia grande, grid assimétrico e microinterações sutis, sem bibliotecas externas.

**Tecnologias:** Python · Django · SQLite · HTML5 · CSS3 · JavaScript · WhiteNoise

## Integrantes

| Nome | Matrícula |
|---|---|
| Giovanni Alves | 01810252 |
| Nicolas Sampaio | 01784117 |
| Matheus Ribeiro | 01802678 |
| Heytor Nascimento | 01792787 |

Disciplina: Frameworks Back-End · Professor: Rafael

## Como executar
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py loaddata produtos      # opcional: carrega os 8 produtos de exemplo
    python manage.py runserver

- Site: http://127.0.0.1:8000/
- Detalhe: http://127.0.0.1:8000/petshop/1/
- Admin: http://127.0.0.1:8000/admin/  (usuário: admin / senha: amigofiel123)

## Testar DEBUG=False
    python manage.py collectstatic
    DEBUG=False python manage.py runserver      # Windows (PowerShell): $env:DEBUG="False"; python manage.py runserver

Os arquivos estáticos são servidos pelo WhiteNoise quando DEBUG=False.

## Onde olhar (para a avaliação)
- `petshop/models.py` — ProdutoPet (nome, preco, estoque, categoria)
- `petshop/views.py` — `ProdutoPet.objects.all()` e `ProdutoPet.objects.get(id=id)`
- `petshop/urls.py` — rota dinâmica `petshop/<int:id>/`
- `petshop/admin.py` — ProdutoPetAdmin
- `petshop/templates/` — index.html (tabela + `{% url %}`), detalhe.html, base.html
- `petshop/static/` — css/estilos.css, js/script.js, images/ (`{% static %}`)

## Licença

O código está sob a licença [MIT](LICENSE). As imagens em `petshop/static/images/` não estão cobertas por ela.

Giovanni Alves, 2026.
