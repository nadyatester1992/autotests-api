from clients.authentication.files.files_client import get_files_client, CreateFileRequestDict
from clients.courses.courses_client import get_courses_client, CreateCoursesRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

# Создаем пользователя
create_users_request = CreateUserRequestDict(
    email = get_random_email(),
    password = "string",
    lastName = "string",
    firstName = "string",
    middleName = "string"
)

create_user_response = public_users_client.create_user(create_users_request)

# Инициализируем клиенты
authentication_user = AuthenticationUserDict(
    email=create_users_request['email'],
    password=create_users_request['password']
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

# Загружаем файл
create_file_request = CreateFileRequestDict(
    filename='image.png',
    directory='courses',
    upload_file='./testdata/files/image.png'
)

create_file_response = files_client.create_file(create_file_request)
print('Create file data: ', create_file_response)

# Создаем курс
create_course_request = CreateCoursesRequestDict(
    title = 'Python',
    maxScore = 100,
    minScore = 1,
    description = 'Python Api Course',
    estimatedTime = '2 week',
    previewFileId = create_file_response['file']['id'],
    createdByUserId = create_user_response['user']['id']
)

create_course_response = courses_client.create_course(create_course_request)
print('Create course data: ', create_course_response)