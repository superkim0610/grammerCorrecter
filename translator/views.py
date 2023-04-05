from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from mainapp.grammerChecker import checkGrammer
import uga_translator

def HTMLTemplate(addition=""):
    navItemName = ["맞춤법", "우가우가"]
    navItemHref = ["check", "translator"] 
    navItem = [[navItemName[i], navItemHref[i]] for i in range(len(navItemName))]
    navItemTag = lambda a, b: f"""
                            <li class="nav-item">
                                <a class="navbar-brand nav-link" href="/{b}/">
                                    {a}
                                </a>
                            </li>"""
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
            <nav class="navbar navbar-expand-lg bg-body-white" sytle="width:100%;">
                <div class="shadow p-3 mb-5 bg-white rounded" style="width:100%;">
                    <ul class="navbar-nav" style="width:auto;">
                        <li class="nav-item">
                            <a class="navbar-brand nav-text" href="/">
                                현재의 우가우가 번역기
                            </a>
                        </li>
                        {"".join([navItemTag(i[0], i[1]) for i in navItem])}
                    </ul>
                </div>
            </nav>
            <div style="width:93%;margin:0 auto;margin-bottom:50px;">
                <div class="alert alert-warning" role="alert">
                    <a class="alert-link" href="/translator/">우가우가<a>
                </div>
            </div>
            {addition}
        </body>
    </html>
    """

def index(request):
    return HttpResponse(HTMLTemplate())

def develop(request):
    request.GET['input']
    HTML = """
    <html>
        <form>
            <input name="input" type="text" />
            <button type="submit">submit</button>
        </form>
    </html>
    """
    return HttpResponse(HTML)