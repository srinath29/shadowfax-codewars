import webbrowser
import json



htmlScript0 = """<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Simple markers</title>
    <style>
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
      #map {
        height: 100%;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>

      function initMap() {


            var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center : {"lat":12.925975583315498, "lng":77.6753354072571}
        });


        """




htmlScriptEnd =       """

      }
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCTVcmF2m7PGO1UgEEv9Mfn-Vo0XbA5XYY&callback=initMap">
    </script>
  </body>
</html>



"""

subJS0 = "var "

subJS1 = """= new google.maps.Marker({
          position:"""

subJSEnd = "     ,map: map"

def processTrail(li):
    di = {}
    for l in range(1,len(li)+1):
        ind = l-1
        if li[ind] not in di:
            di[li[ind]] = str(l)
        else:
            di[li[ind]] = di[li[ind]] +"," +str(l)
    i = 1
    marker = "marker"
    inScript = ""
    end =  "});\n"

    for key in di:
        lats = json.dumps({"lat":float(key[0]), "lng":float(key[1])})
        marker = marker+ str(i)
        i+=1
        title = "title: '" + str(di[key])+"'"
        inScript = inScript +subJS0 + marker +subJS1 + lats +","+ title +subJSEnd + end


    htmlScript = htmlScript0 + inScript + htmlScriptEnd
    print(htmlScript)
    with open("k.html", "w") as f:
        f.write(htmlScript)

    webbrowser.open("k.html")
