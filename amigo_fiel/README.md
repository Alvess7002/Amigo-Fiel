# Amigo Fiel — catálogo de produtos pet (Django)

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
