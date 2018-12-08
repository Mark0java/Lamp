import json
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import On_Off, Bright, Rotations, Up_down
from dialogflow_lite.dialogflow import Dialogflow


def convert(data):
    if isinstance(data, bytes):
        return data.decode('ascii')
    if isinstance(data, dict):
        return dict(map(convert, data.items()))
    if isinstance(data, tuple):
        return map(convert, data)

    return data

@csrf_exempt
def view_store(request):
    client_access_token = 'a4074b8968b642569227649d49ea41eb'
    dialogflow = Dialogflow(client_access_token=client_access_token)
    input_dict = convert(request.body)
    action = json.loads(input_dict)['queryResult']['action']
    parameters = json.loads(input_dict)['queryResult']['parameters']
    if request.method == "POST":
        if (action == 'on_off'):
            if (str(parameters['switch_state']) == 'on'):
                On_Off(
                    on_off=1,
                ).save()
            if (str(parameters['switch_state']) == 'off'):
                On_Off(
                    on_off=0,
                ).save()

        if (action == 'rotation'):
            if (str(parameters['side']) == 'left'):
                Rotations(
                    corner=-1*parameters['rotate']
                ).save()
            if (str(parameters['side']) == 'right'):
                Rotations(
                    corner=parameters['rotate']
                ).save()

        if(action == 'brightness'):
            Bright(
                bright=parameters['bright']
            ).save()

        if (action == 'up_down'):
            if (str(parameters['up_down']) == 'down'):
                print(parameters['value'])
                Up_down(
                    up_down=-1 * parameters['value']
                ).save()
            if (str(parameters['up_down']) == 'up'):
                print(parameters['value'])
                Up_down(
                    up_down=parameters['value']
                ).save()



    data = {'fulfillmentText': json.loads(input_dict)['queryResult']['fulfillmentText'], 'fulfillmentMessages': json.loads(input_dict)['queryResult']['fulfillmentMessages']}
    return HttpResponse(json.dumps(data))


@csrf_exempt
def get_on_off(request):
    switch_state = dict(request.POST)
    result = {'status': 'ok', 'switch_state': switch_state}
    print(switch_state)
    On_Off(
        on_off=(switch_state['switch_state'][0]),
    ).save()
    return HttpResponse(json.dumps(result))

@csrf_exempt
def get_rotations(request):
    data = dict(request.POST)
    result = {'status': 'ok', 'corner': data}
    print(data)
    Rotations(
        corner=(data['corner'][0]),
    ).save()
    return HttpResponse(json.dumps(result))

@csrf_exempt
def get_brightness(request):
    bright = dict(request.POST)
    result = {'status': 'ok', 'bright': bright}
    print(bright)
    Bright(
        bright=(bright['bright'][0]),
    ).save()
    return HttpResponse(json.dumps(result))

@csrf_exempt
def send_on_off(request):
    result = []
    ind_on = On_Off.objects.latest('timestamp')
    print(ind_on)
    result.append({'on_off': ind_on.on_off})
    return HttpResponse(json.dumps(result, indent=4))

@csrf_exempt
def send_brightness(request):
    result = []
    ind_bright = Bright.objects.latest('timestamp')
    print(ind_bright)
    result.append({'bright': ind_bright.bright})
    return HttpResponse(json.dumps(result, indent=4))

@csrf_exempt
def send_rotations(request):
    result = []
    ind_rotate = Rotations.objects.latest('timestamp')
    print(ind_rotate)
    result.append({'corner': ind_rotate.corner})
    return HttpResponse(json.dumps(result, indent=4))

@csrf_exempt
def send_up_down(request):
    result = []
    ind_up_down = Up_down.objects.latest('timestamp')
    print(ind_up_down)
    result.append({'up_down': ind_up_down.up_down})
    return HttpResponse(json.dumps(result, indent=4))

@csrf_exempt
def get_up_down(request):
    up_down = dict(request.POST)
    result = {'status': 'ok', 'up_down': up_down}
    print(up_down)
    Up_down(
        up_down=(up_down['up_down'][0]),
    ).save()
    return HttpResponse(json.dumps(result))

# def view_info(request):
#     result = []
#     try:
#         ind = Indicators.objects.latest('timestamp')
#         result.append({'W': ind.W, 'A': ind.A, 'V': ind.V, 'socket_id': ind.socket_id})
#     except Indicators.DoesNotExist:
#         pass
#     return HttpResponse(json.dumps(result, indent=4))


# def view_history(request):
#     result = []
#     try:
#         result = [{'W': ind.W, 'A': ind.A, 'V': ind.V, 'socket_id': ind.socket_id, "timestamp": str(ind.timestamp)} for
#                   ind in Indicators.objects.all()]
#     except Indicators.DoesNotExist:
#         pass
#     return HttpResponse(json.dumps(result, indent=4))


# def sendbrightnees(request):


# @csrf_exempt
# def view_store(request):
#     indicators = dict(request.POST)
#     result = {'status': 'ok', 'indicators': indicators}
#
#     Indicators(
#         A=float(indicators['A'][0]),
#         V=float(indicators['V'][0]),
#         W=float(indicators['W'][0]),
#         socket_id=int(indicators['socket_id'][0]),
#     ).save()
#     return HttpResponse(json.dumps(result))


# @csrf_exempt
# def view_set_on_off(request):
#     if request.method == "POST":
#         value = dict(request.POST).get('swich_state')
#         # print("Server retrieved data from mobile: '%s'. Save to database: %s" % (on_off, value))
#         # DO NOT PRINT ANYTHING !!!!!!  use .format instead %
#         if value and isinstance(value, list):
#             value = value[0]
#             o, is_new = On_Off.objects.get_or_create(user=request.user.id, on_off=value)
#             o.save()
#             return HttpResponse(json.dumps({'status': 'ok', 'on_off': value}))
#     return HttpResponse(json.dumps({'status': 'invalid'}))

# def view_store(request):
#     client_access_token = 'a4074b8968b642569227649d49ea41eb'
#     dialogflow = Dialogflow(client_access_token=client_access_token)
#     input_dict = convert(request.body)
#     input_text = json.loads(input_dict)['queryResult']['parameters']
#     responses = dialogflow.text_request(str(input_text))
#     print(input_text)
#     Indicators(
#         A=float(input_text['A']),
#         V=float(input_text['V']),
#         W=float(input_text['W']),
#         socket_id=float(input_text['socket_id']),
#     ).save()
#
#     if request.method == "POST":
#         data = {'': 'ok'}
#         return JsonResponse(data, status=200)


