import json, urllib2, utils
#google embed maps api key: AIzaSyC3JS6akFEzmQqhsa_ny3OoqEt3gDOAWow
#link: https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=YOUR_API_KEY

def getMapLink(origin, dest):
    url="""https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&key=AIzaSyC3JS6akFEzmQqhsa_ny3OoqEt3gDOAWow
"""
    fixedOrigin=utils.spaceConverter(origin)
    fixedDest=utils.spaceConverter(dest)
    url=url%(fixedOrigin)
    url=url%(fixedDest)
    return url
