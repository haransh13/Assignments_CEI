import json
   
json_data = {"copyright":"Jes\u00fas Carmona Guill\u00e9n",
             "date":"2024-07-04",
             "explanation":"The beautiful Trifid Nebula is a cosmic study in contrasts. Also known as M20, it lies about 5,000 light-years away toward the nebula rich constellation Sagittarius. A star forming region in the plane of our galaxy, the Trifid does illustrate three different types of astronomical nebulae; red emission nebulae dominated by light from hydrogen atoms, blue reflection nebulae produced by dust reflecting starlight, and dark nebulae where dense dust clouds appear in silhouette. But the red emission region, roughly separated into three parts by obscuring dust lanes, is what lends the Trifid its popular name. Pillars and jets sculpted by newborn stars, above and right of the emission nebula's center, appear in famous Hubble Space Telescope close-up images of the region. The Trifid Nebula is about 40 light-years across. Too faint to be seen by the unaided eye, it almost covers the area of a full moon on planet Earth's sky.",
             "hdurl":"https://apod.nasa.gov/apod/image/2407/TrifidrecortesRGB.jpg",
             "media_type":"image",
             "service_version":"v1",
             "title":"A Beautiful Trifid",
             "url":"https://apod.nasa.gov/apod/image/2407/TrifidrecortesRGB1024.jpg"
             }

print("Explanation:", json_data["explanation"])
print("\n Title:", json_data["title"])