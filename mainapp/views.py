from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from mainapp.grammerChecker import checkGrammer

def HTMLTemplate(addition=""):
    return f"""
    <html>
        <!--<link rel="shortcut icon" href="/favicon.ico"/>-->
        <!--fonts-->
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;700;800;900&display=swap" rel="stylesheet">
        <!--bootstrap-->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
        <head>
            <title></title>
            <style>
                body {{
                    font-family: 'Noto Sans KR', sans-serif;
                }}
                .nav-text {{
                    font-weight: 700;
                    font-size:25px;
                }}
                
                p {{
                    float: left;
                    margin-right: 8px;
                    font-weight: 300;
                }}
                h5 {{
                    font-weight:500
                }}
                .redText {{
                    color: red;
                    //font-weight: bold;
                }}
                .blueText {{
                    color: blue;
                    //font-weight: bold;
                }}
                .list {{
                    margin-left: 10%;
                    margin-right: 10%;
                }}
                .re-check-button {{
                    margin-top: 30px;
                }}
            </style>
        </head>
        <body>
            <!--<nav class="navbar bg-body-tertiary bg-secondary">
                <div class="container-fluid">
                    <a class="navbar-brand text-white" href="#">
                        현재의 맞춤법 검사기
                    </a>
                </div>
            </nav>-->
            <nav>
                <div class="shadow p-3 mb-5 bg-white rounded">
                    <a class="navbar-brand nav-text" href="#">
                            현재의 맞춤법 검사기
                    </a>
                </div>
            </nav>
            {addition}
        </body>
    </html>
    """

def resultTemplate(grammerData):
    if grammerData['isErr'] == [False]:
        resultTag = f"""
            <div class="list-group list text center">
                <a href="#" class="list-group-item list-group-item-action active list-group-item-primary" aria-current="true">
                    <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">오류가 없습니다</h5>
                    </div>
                    <p class="mb-1">{" ".join(grammerData['orgTextList'])}</p>
                </a>
                <button type="submit" class="btn btn-secondary mb-3 re-check-button" onclick="location.href=/check/">다시 검사</button>
            </div>
        """
    else:
        resultTag = f"""
            <div class="list-group list text-center">
                <a href="#" class="list-group-item list-group-item-action active list-group-item-danger" aria-current="true">
                    <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">수정 전</h5>
                    </div>
                    <p class="mb-1">{" ".join(grammerData['orgTextList'])}</p>
                </a>
                <a href="#" class="list-group-item list-group-item-action">
                    <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">수정 후</h5>
                    </div>
                    <p class="mb-1">{" ".join(grammerData['candTextList'])}</p>
                </a>
                <button type="submit" class="btn btn-secondary mb-3 re-check-button" onclick="location.href=/check/">다시 검사</button>
            </div>
        """
    return resultTag

@csrf_exempt
def index(request):
    return redirect('./check/')

@csrf_exempt
def check(request):
    formTag = """
    <form action="/result/" method="POST">
        <input type="text" name="input_text"/>
        <button type="submit">submit</button>
    </form>
    """
    _formTag = """
        <center>
            <div style="width:60%;">
                <form class="row g-3" action="/result/" method="POST">
                    <div class="col-auto">
                        <label for="inputText" class="visually-hidden">input text</label>
                        <input type="text" class="form-control" id="inputText" placeholder="뭐라도 써봐" name="input_text">
                    </div>
                    <div class="col-auto">
                        <button type="submit" class="btn btn-secondary mb-3">검사</button>
                    </div>
                </form>
            </div>
        </center>
    """
    return HttpResponse(HTMLTemplate(_formTag))

@csrf_exempt
def result(request):
    input_text = request.POST["input_text"]
    grammerData = checkGrammer(input_text)
    resultTag = resultTemplate(grammerData)
    return HttpResponse(HTMLTemplate(resultTag))