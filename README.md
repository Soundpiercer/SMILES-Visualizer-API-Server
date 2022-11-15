# Visualizer-API-Server Set up

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

# TODO
- [x] User login
- [x] User signup
- [ ] detail에 표시될 분자식에 대한 정보는 어떻게 저장하며 처리할 것인지
- [ ] save as a file은 unity에서 할 수 있나?
- [ ] 평소에는 그냥 검색할 수 있다가 Save 기능을 사용하기 위해서 or Saved list로 들어가기 위해서는 login required
- [ ] compare 버튼을 누르면 compare algorithm 실행 R&D 중인 algorithm 호출
- [ ] login 하라는 warning 띄어주기