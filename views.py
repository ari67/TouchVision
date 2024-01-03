from django.shortcuts import render, redirect
from django.http import HttpResponse

import cv2
from PIL import Image
import numpy as np
import os

import tensorflow as tf
from django.conf import settings
from django.template.response import TemplateResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

from django.core.files.storage import FileSystemStorage

# Create your views here.
#@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile_updated')  # Redirect to a success page
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'profile_update.html', {'form': form})


def index(request):
	return render(request, 'index.html')

def Home(request):
	return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            check = "Password and Re-entered Password doesn't match"
            return render(request, "signup.html", {"check": check})
        else:
            # Use Django's built-in method for user creation
            user = User.objects.create_user(username, email, password1)
            user.save()

            # Automatically log the user in after registration
            login(request, user)

            return render(request, 'index.html')

    return render(request, "signup.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            check = "Username or Password is incorrect!"
            return render(request, "user_login.html", {"check": check})

    return render(request, "user_login.html")

def About(request):
    return render(request, 'About.html')

def Learn_Braille(request):
	return render(request, 'Learn_Braille.html')
    
def Word_Game(request):
    return render(request, 'Word_Game.html')

def Ant (request):
    return render(request, 'Ant.html')

def Bat(request):
    return render(request, 'Bat.html')

def Cat(request):
    return render(request, 'Cat.html')

class CustomFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length = None):
        self.delete(name)
        return name

#End of Some functions
#--------------------------------------------------------------------------------------------------------------

def Letter_A(request):
    
    message = ""
    prediction = ""

    fss = CustomFileSystemStorage()

    try:
        image = request.FILES["image"]
        print("Name: ", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" +image.name
        #path = os.path.join(settings.MEDIA_ROOT, image.name)
        #image details
        image_url = fss.url(_image)
        #Read the image
        image = cv2.imread(path)
        name_letter = os.path.basename(path)[0]
        image_arr = np.array(image)
        name_arr = np.array(name_letter)
        resize_image = image_arr/255.0

        test_image = np.expand_dims(resize_image, axis = 0)

        #load model

        model = tf.keras.models.load_model(os.getcwd() + '/BCR1.h5')

        result = model.predict(test_image)

        #----------------------------------

        print("Prediction: ", str(np.argmax(result)))

        if(np.argmax(result) == 0):
            prediction = "Correct Answer!!"
            check = "Congratulations"
            

        else:
            prediction = "Wrong Answer!"
            check = "Try Again!"
            

        return TemplateResponse(request, "Letter_A.html",
            {
                "image": image,
                "prediction": prediction,
                "check": check

            }
            )
    except MultiValueDictKeyError:
        return TemplateResponse(
            request,
            "Letter_A.html",
            {"message": "No Image Selected"
            })

#End of Letter_A
#---------------------------------------------------------------------------------------------------------------
def Letter_B(request):
    message = ""
    prediction = ""

    fss = CustomFileSystemStorage()

    try:
        image = request.FILES["image"]
        print("Name: ", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" +image.name
        #path = os.path.join(settings.MEDIA_ROOT, image.name)
        #image details
        image_url = fss.url(_image)
        #Read the image
        image = cv2.imread(path)
        name_letter = os.path.basename(path)[0]
        image_arr = np.array(image)
        name_arr = np.array(name_letter)
        resize_image = image_arr/255.0

        test_image = np.expand_dims(resize_image, axis = 0)

        #load model

        model = tf.keras.models.load_model(os.getcwd() + '/BCR1.h5')

        result = model.predict(test_image)

        #----------------------------------

        print("Prediction: ", str(np.argmax(result)))

        if(np.argmax(result) == 1):
            prediction = "Correct Answer!!"
            check = "Congratulations"

        else:
            prediction = "Wrong Answer!"
            check = "Try Again!"

        return TemplateResponse(request, "Letter_B.html",
            {
                "image": image,
                "prediction": prediction,
                "check": check

            }
            )
    except MultiValueDictKeyError:
        return TemplateResponse(
            request,
            "Letter_B.html",
            {"message": "No Image Selected"
            })

#End of Letter_B
#-------------------------------------------------------------------------------------------------------------
def Letter_C(request):
    message = ""
    prediction = ""

    fss = CustomFileSystemStorage()

    try:
        image = request.FILES["image"]
        print("Name: ", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" +image.name
        #path = os.path.join(settings.MEDIA_ROOT, image.name)
        #image details
        image_url = fss.url(_image)
        #Read the image
        image = cv2.imread(path)
        name_letter = os.path.basename(path)[0]
        image_arr = np.array(image)
        name_arr = np.array(name_letter)
        resize_image = image_arr/255.0

        test_image = np.expand_dims(resize_image, axis = 0)

        #load model

        model = tf.keras.models.load_model(os.getcwd() + '/BCR1.h5')

        result = model.predict(test_image)

        #----------------------------------

        print("Prediction: ", str(np.argmax(result)))

        if(np.argmax(result) == 2):
            prediction = "Correct Answer!!"
            check = "Congratulations"

        else:
            prediction = "Wrong Answer!"
            check = "Try Again!"

        return TemplateResponse(request, "Letter_C.html",
            {
                "image": image,
                "prediction": prediction,
                "check": check

            }
            )
    except MultiValueDictKeyError:
        return TemplateResponse(
            request,
            "Letter_C.html",
            {"message": "No Image Selected"
            })

#End of Letter_C
#---------------------------------------------------------------------------------------------------------------
################################################################################################################
#WORD ANT

def Ant_a(request):
    request.session['flag_ant'] = 0
    message = ""
    prediction_a = ""
    print("I'm inside Ant_a")

    fss = CustomFileSystemStorage()


    try:
        print("I'm inside Ant_a try1")

        image = request.FILES["image"]
        print("I'm inside Ant_a try1 image")

        print("Name: ", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" +image.name
        print(path)

        #path = os.path.join(settings.MEDIA_ROOT, image.name)
        #image details
        image_url = fss.url(_image)
        #Read the image
        image = cv2.imread(path)
        name_letter = os.path.basename(path)[0]
        image_arr = np.array(image)
        name_arr = np.array(name_letter)
        resize_image = image_arr/255.0

        test_image = np.expand_dims(resize_image, axis = 0)
        print("I'm inside Ant_a test")

        #load model

        model = tf.keras.models.load_model(os.getcwd() + '/BCR1.h5')

        result = model.predict(test_image)

        #----------------------------------

        print("Prediction: ", str(np.argmax(result)))

        if(np.argmax(result) == 0):
            #print('hello')
            prediction_a = "Correct Answer!!"
            #check = "Congratulations"
            request.session['flag_ant'] += 1

        else:
            prediction_a = "Wrong Answer!"
            #check = "Try Again!"
            #request.session['flag_ant'] += 0
        print(prediction_a)
        return TemplateResponse(request, "Ant.html",
            {
                "image": image,
                "prediction_a": prediction_a,
                #"check": check

            }
            )
    except MultiValueDictKeyError:
        return TemplateResponse(
            request,
            "Ant.html",
            {"message": "No Image Selected"
            })   

def Ant_n(request):
    message = ""
    prediction_n = ""
    print("I'm inside Ant_n")

    fss = CustomFileSystemStorage()


    try:
        print("I'm inside Ant_n try1")

        image = request.FILES["image"]
        print("I'm inside Ant_a try1 image")

        print("Name: ", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" +image.name
        print(path)

        #path = os.path.join(settings.MEDIA_ROOT, image.name)
        #image details
        image_url = fss.url(_image)
        #Read the image
        image = cv2.imread(path)
        name_letter = os.path.basename(path)[0]
        image_arr = np.array(image)
        name_arr = np.array(name_letter)
        resize_image = image_arr/255.0

        test_image = np.expand_dims(resize_image, axis = 0)
        print("I'm inside Ant_a test")

        #load model

        model = tf.keras.models.load_model(os.getcwd() + '/BCR1.h5')

        result = model.predict(test_image)

        #----------------------------------

        print("Prediction: ", str(np.argmax(result)))

        if(np.argmax(result) == 13):
            #print('hello')
            prediction_n = "Correct Answer!!"
            #check = "Congratulations"
            request.session['flag_ant'] += 1

        else:
            prediction_n = "Wrong Answer!"
            #check = "Try Again!"
            #request.session['flag_ant'] += 0
        print(prediction_n)
        return TemplateResponse(request, "Ant.html",
            {
                "image": image,
                "prediction_n": prediction_n,
                #"check": check

            }
            )
    except MultiValueDictKeyError:
        return TemplateResponse(
            request,
            "Ant.html",
            {"message": "No Image Selected"
            }) 
def Ant_t(request):
    message = ""
    prediction_t = ""
    final_message = ""
    print("I'm inside Ant_t")

    fss = CustomFileSystemStorage()


    try:
        print("I'm inside Ant_t try1")

        image = request.FILES["image"]
        print("I'm inside Ant_t try1 image")

        print("Name: ", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" +image.name
        print(path)

        #path = os.path.join(settings.MEDIA_ROOT, image.name)
        #image details
        image_url = fss.url(_image)
        #Read the image
        image = cv2.imread(path)
        name_letter = os.path.basename(path)[0]
        image_arr = np.array(image)
        name_arr = np.array(name_letter)
        resize_image = image_arr/255.0

        test_image = np.expand_dims(resize_image, axis = 0)
        print("I'm inside Ant_t test")

        #load model

        model = tf.keras.models.load_model(os.getcwd() + '/BCR1.h5')

        result = model.predict(test_image)

        #----------------------------------

        print("Prediction: ", str(np.argmax(result)))

        if(np.argmax(result) == 19):
            #print('hello')
            prediction_t = "Correct Answer!!"
            #check = "Congratulations"
            request.session['flag_ant'] += 1

        else:
            prediction_t = "Wrong Answer!"
            #check = "Try Again!"
            #request.session['flag_ant'] += 0
        print(prediction_t)
        print(request.session['flag_ant'])

        if request.session['flag_ant'] == 3:
            final_message = "Congratulations !!!"

        else: 
            final_message = "Try Again :("
        
        return TemplateResponse(request, "Ant.html",
            {
                "image": image,
                "prediction_t": prediction_t,
                #"check": check
                "final_message": final_message

            }
            )
    except MultiValueDictKeyError:
        return TemplateResponse(
            request,
            "Ant.html",
            {"message": "No Image Selected"
            }) 

######################################################################################################
#----------------------------------------------------------------------------------------------------
#WORD BAT
def Bat_b(request):
    request.session['flag_bat'] = 0
    message = ""
    prediction_a = ""
    print("I'm inside bat_b")

    fss = CustomFileSystemStorage()


    try:
        print("I'm inside Ant_a try1")

        image = request.FILES["image"]
        print("I'm inside Ant_a try1 image")

        print("Name: ", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" +image.name
        print(path)

        #path = os.path.join(settings.MEDIA_ROOT, image.name)
        #image details
        image_url = fss.url(_image)
        #Read the image
        image = cv2.imread(path)
        name_letter = os.path.basename(path)[0]
        image_arr = np.array(image)
        name_arr = np.array(name_letter)
        resize_image = image_arr/255.0

        test_image = np.expand_dims(resize_image, axis = 0)
        print("I'm inside Ant_a test")

        #load model

        model = tf.keras.models.load_model(os.getcwd() + '/BCR1.h5')

        result = model.predict(test_image)

        #----------------------------------

        print("Prediction: ", str(np.argmax(result)))

        if(np.argmax(result) == 1):
            #print('hello')
            prediction_b = "Correct Answer!!"
            #check = "Congratulations"
            request.session['flag_bat'] += 1

        else:
            prediction_b = "Wrong Answer!"
            #check = "Try Again!"
            #request.session['flag_ant'] += 0
        print(prediction_b)
        return TemplateResponse(request, "Bat.html",
            {
                "image": image,
                "prediction_b": prediction_b,
                #"check": check

            }
            )
    except MultiValueDictKeyError:
        return TemplateResponse(
            request,
            "Bat.html",
            {"message": "No Image Selected"
            })   

def Bat_a(request):
    message = ""
    prediction_a = ""
    print("I'm inside Ant_n")

    fss = CustomFileSystemStorage()


    try:
        print("I'm inside Ant_n try1")

        image = request.FILES["image"]
        print("I'm inside Ant_a try1 image")

        print("Name: ", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" +image.name
        print(path)

        #path = os.path.join(settings.MEDIA_ROOT, image.name)
        #image details
        image_url = fss.url(_image)
        #Read the image
        image = cv2.imread(path)
        name_letter = os.path.basename(path)[0]
        image_arr = np.array(image)
        name_arr = np.array(name_letter)
        resize_image = image_arr/255.0

        test_image = np.expand_dims(resize_image, axis = 0)
        print("I'm inside Ant_a test")

        #load model

        model = tf.keras.models.load_model(os.getcwd() + '/BCR1.h5')

        result = model.predict(test_image)

        #----------------------------------

        print("Prediction: ", str(np.argmax(result)))

        if(np.argmax(result) == 0):
            #print('hello')
            prediction_a = "Correct Answer!!"
            #check = "Congratulations"
            request.session['flag_bat'] += 1

        else:
            prediction_a = "Wrong Answer!"
            #check = "Try Again!"
            #request.session['flag_ant'] += 0
        print(prediction_a)
        return TemplateResponse(request, "Bat.html",
            {
                "image": image,
                "prediction_a": prediction_a,
                #"check": check

            }
            )
    except MultiValueDictKeyError:
        return TemplateResponse(
            request,
            "Bat.html",
            {"message": "No Image Selected"
            }) 
def Bat_t(request):
    message = ""
    prediction_t = ""
    final_message = ""
    print("I'm inside Ant_t")

    fss = CustomFileSystemStorage()


    try:
        print("I'm inside Ant_t try1")

        image = request.FILES["image"]
        print("I'm inside Ant_t try1 image")

        print("Name: ", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" +image.name
        print(path)

        #path = os.path.join(settings.MEDIA_ROOT, image.name)
        #image details
        image_url = fss.url(_image)
        #Read the image
        image = cv2.imread(path)
        name_letter = os.path.basename(path)[0]
        image_arr = np.array(image)
        name_arr = np.array(name_letter)
        resize_image = image_arr/255.0

        test_image = np.expand_dims(resize_image, axis = 0)
        print("I'm inside Ant_t test")

        #load model

        model = tf.keras.models.load_model(os.getcwd() + '/BCR1.h5')

        result = model.predict(test_image)

        #----------------------------------

        print("Prediction: ", str(np.argmax(result)))

        if(np.argmax(result) == 19):
            #print('hello')
            prediction_t = "Correct Answer!!"
            #check = "Congratulations"
            request.session['flag_bat'] += 1

        else:
            prediction_t = "Wrong Answer!"
            #check = "Try Again!"
            #request.session['flag_ant'] += 0
        print(prediction_t)
        print(request.session['flag_bat'])

        if request.session['flag_bat'] == 3:
            final_message = "Congratulations !!!"

        else: 
            final_message = "Try Again :("
        
        return TemplateResponse(request, "Bat.html",
            {
                "image": image,
                "prediction_t": prediction_t,
                #"check": check
                "final_message": final_message

            }
            )
    except MultiValueDictKeyError:
        return TemplateResponse(
            request,
            "Bat.html",
            {"message": "No Image Selected"
            }) 

#############################################################################################
#--------------------------------------------------------------------------------------------
#WORD CAT
def Cat_c(request):
    request.session['flag_cat'] = 0
    message = ""
    prediction_c = ""
    print("I'm inside bat_b")

    fss = CustomFileSystemStorage()


    try:
        print("I'm inside Ant_a try1")

        image = request.FILES["image"]
        print("I'm inside Ant_a try1 image")

        print("Name: ", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" +image.name
        print(path)

        #path = os.path.join(settings.MEDIA_ROOT, image.name)
        #image details
        image_url = fss.url(_image)
        #Read the image
        image = cv2.imread(path)
        name_letter = os.path.basename(path)[0]
        image_arr = np.array(image)
        name_arr = np.array(name_letter)
        resize_image = image_arr/255.0

        test_image = np.expand_dims(resize_image, axis = 0)
        print("I'm inside Ant_a test")

        #load model

        model = tf.keras.models.load_model(os.getcwd() + '/BCR1.h5')

        result = model.predict(test_image)

        #----------------------------------

        print("Prediction: ", str(np.argmax(result)))

        if(np.argmax(result) == 2):
            #print('hello')
            prediction_c = "Correct Answer!!"
            #check = "Congratulations"
            request.session['flag_cat'] += 1

        else:
            prediction_c = "Wrong Answer!"
            #check = "Try Again!"
            #request.session['flag_ant'] += 0
        print(prediction_c)
        return TemplateResponse(request, "Cat.html",
            {
                "image": image,
                "prediction_c": prediction_c,
                #"check": check

            }
            )
    except MultiValueDictKeyError:
        return TemplateResponse(
            request,
            "Cat.html",
            {"message": "No Image Selected"
            })   

def Cat_a(request):
    message = ""
    prediction_a = ""
    print("I'm inside Ant_n")

    fss = CustomFileSystemStorage()


    try:
        print("I'm inside Ant_n try1")

        image = request.FILES["image"]
        print("I'm inside Ant_a try1 image")

        print("Name: ", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" +image.name
        print(path)

        #path = os.path.join(settings.MEDIA_ROOT, image.name)
        #image details
        image_url = fss.url(_image)
        #Read the image
        image = cv2.imread(path)
        name_letter = os.path.basename(path)[0]
        image_arr = np.array(image)
        name_arr = np.array(name_letter)
        resize_image = image_arr/255.0

        test_image = np.expand_dims(resize_image, axis = 0)
        print("I'm inside Ant_a test")

        #load model

        model = tf.keras.models.load_model(os.getcwd() + '/BCR1.h5')

        result = model.predict(test_image)

        #----------------------------------

        print("Prediction: ", str(np.argmax(result)))

        if(np.argmax(result) == 0):
            #print('hello')
            prediction_a = "Correct Answer!!"
            #check = "Congratulations"
            request.session['flag_cat'] += 1

        else:
            prediction_a = "Wrong Answer!"
            #check = "Try Again!"
            #request.session['flag_ant'] += 0
        print(prediction_a)
        return TemplateResponse(request, "Cat.html",
            {
                "image": image,
                "prediction_a": prediction_a,
                #"check": check

            }
            )
    except MultiValueDictKeyError:
        return TemplateResponse(
            request,
            "Cat.html",
            {"message": "No Image Selected"
            }) 
def Cat_t(request):
    message = ""
    prediction_t = ""
    final_message = ""
    print("I'm inside Ant_t")

    fss = CustomFileSystemStorage()


    try:
        print("I'm inside Ant_t try1")

        image = request.FILES["image"]
        print("I'm inside Ant_t try1 image")

        print("Name: ", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" +image.name
        print(path)

        #path = os.path.join(settings.MEDIA_ROOT, image.name)
        #image details
        image_url = fss.url(_image)
        #Read the image
        image = cv2.imread(path)
        name_letter = os.path.basename(path)[0]
        image_arr = np.array(image)
        name_arr = np.array(name_letter)
        resize_image = image_arr/255.0

        test_image = np.expand_dims(resize_image, axis = 0)
        print("I'm inside Ant_t test")

        #load model

        model = tf.keras.models.load_model(os.getcwd() + '/BCR1.h5')

        result = model.predict(test_image)

        #----------------------------------

        print("Prediction: ", str(np.argmax(result)))

        if(np.argmax(result) == 19):
            #print('hello')
            prediction_t = "Correct Answer!!"
            #check = "Congratulations"
            request.session['flag_cat'] += 1

        else:
            prediction_t = "Wrong Answer!"
            #check = "Try Again!"
            #request.session['flag_ant'] += 0
        print(prediction_t)
        print(request.session['flag_cat'])

        if request.session['flag_cat'] == 3:
            final_message = "Congratulations !!!"

        else: 
            final_message = "Try Again :("
        
        return TemplateResponse(request, "Cat.html",
            {
                "image": image,
                "prediction_t": prediction_t,
                #"check": check
                "final_message": final_message

            }
            )
    except MultiValueDictKeyError:
        return TemplateResponse(
            request,
            "Cat.html",
            {"message": "No Image Selected"
            }) 

