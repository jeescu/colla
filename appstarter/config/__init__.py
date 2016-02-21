__author__ = 'john'

# session token expires
expires = 8

environment = 'development'

# model: images upload path set
post_image_upload_path = 'appstarter/static/colla/images/post_img/'
profile_image_upload_path = 'appstarter/static/colla/images/profile_img/'

# concats image path indexes
env_img_concat_index = 10


if environment == 'production':
    post_image_upload_path = 'ProStarter/appstarter/static/colla/images/post_img/'
    proile_image_upload_path = 'ProStarter/appstarter/static/colla/images/profile_img/'
    env_img_concat_index = 21