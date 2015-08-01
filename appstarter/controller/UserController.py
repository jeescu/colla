from appstarter.models import User
from appstarter.forms import UserForm, ProfileForm
from appstarter.controller import AuthController
from appstarter.services import AuthService
from appstarter.utils import ResponseParcel


class UserController(object):

    def __init__(self):
        pass

    def index(self, request):
        response = ResponseParcel.ResponseParcel()
        response.set_uri('/colla/')
        return response.redirect()

    def login(self, request):

        login = AuthController.AuthController()
        return login.app_login(request)

    def register(self, request):
        response = ResponseParcel.ResponseParcel()
        response.set_uri('colla/signup.html')
        return response.render(request)
        
    def do_register(self, request):

        response = ResponseParcel.ResponseParcel()
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        try:

            if user_form.is_valid():
                new_user = User(
                    username=request.POST['username'],
                    password=request.POST['password'],
                    fullname=request.POST['first_name']
                )

                if profile_form.is_valid():
                    new_user.save()
                    new_user.profile_set.create(
                        dis_name=request.POST['first_name'],
                        profile_pic="/static/colla/images/profile_img/av-default.png",
                        first_name=request.POST['first_name'],
                        last_name=request.POST['last_name'],
                        middle_name=request.POST['middle_name'],
                        position=request.POST['position'],
                        company_name=request.POST['company'],
                        mail_address=request.POST['mail']
                    )

                    response.set_message("Success")
                    return response.to_json()

            else:
                response.set_message("Error")
                response.has_error()
                return response.to_json()
        
        except Exception as e:
            print e

            response.has_error()
            return response.to_json()

    def logout(self, request):
        response = ResponseParcel.ResponseParcel()

        auth_service = AuthService.AuthService()
        auth_service.set_request_data(request)
        auth_service.end_session()

        response.set_uri('/colla/')
        return response.redirect()
