from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from controller.credit_analyzer import CreditAnalyzer

async def homepage(request):
    return JSONResponse({'hello': 'world'})

async def analyzer_route(request):
    body = await request.json()
    credit_controller = CreditAnalyzer(body["customer"])
    return JSONResponse({
        "credit_granted": credit_controller.grant_credit(),
        "value": credit_controller.credit_granted()
    })

app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/analyze', analyzer_route, methods=['POST'])
])