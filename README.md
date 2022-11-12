# Moflow+ Project Set up

clone 해서 사용할 시

```
pip install --upgrade --force-reinstall -r requirements.txt
```

## Project structure에 대한 설명

## moflow+

    settings 관련 파일들이 있음
    high-level의 urls

## core

    실제로 기능을 구현하는 곳

core directory 아래에 있는 파일에 대한 간략한 설명

- models.py

  database의 model 정의

- forms.py

  어떤 형태로 데이터를 받을지 폼 관리

- test.py

  테스팅

- views.py

  get, post 등 method 구현

- urls.py

  view 혹은 function을 특정 url에 연결

## templates

    html 파일

## static_in_env

    css, js, image, font 등
