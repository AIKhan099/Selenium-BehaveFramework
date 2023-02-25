FROM python:3.9.12
WORKDIR /code

COPY requirements.txt /code/requirements.txt
# F:\courses\behave framework\test\features\test1.feature
# COPY ./features/test1.feature /code/features/test1.feature
# COPY ./features/test1.feature /code/features/test1.feature
COPY ./features /code/features
COPY ./reports /code/reports


RUN pip install -r requirements.txt
# RUN poetry config virtualenvs.create false
# RUN poetry install --no-dev


CMD [ "python", "./features/test1.feature", "behave -f allure_behave.formatter:AllureFormatter -o ./reports/ ./features/test1.feature"]
# RUN behave -f allure_behave.formatter:AllureFormatter -o reports/ features\test1.feature