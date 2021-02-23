# Recipe Book Project

### Planning Story
While considering creating this API, I begun with a simpler idea of creating an
application which was going to allow users to create profiles to job hunt (sort of
like a linkedIn or zipRecruiter). However after some consideration I decided to
create a interactive site/forum which allowed users to create profiles in order to
receive critisism from other people regarding their resume, elevator pitch, etc.
This allowed me to know that I will initially need a few models, a user model, a
profile model (which I named RecruitMe(FOR NOW)) and a comment model which I will
name Comment.

### Development Process
I began by making sure that the user model was working properly and had all of
attributes that are required of it. I then followed the process that was taught in
class in creating a new model for our RecruitMe profile, I created the model, made
migrations and migrated. I created URL paths, added it to the admin panel, created
serializers and views for the user model. I deployed the application to heroku
with no issues. I then ran curl-scrips for all of the functionality in order to
make sure everything was working properly before I began working on my front-end.

### Link to Front-end Repo
[Front-end Repo](https://github.com/sergegg/recruitMe-client)

### Strategy to Solve Problems
My strategy to solve problems was reffering to the documintation, referring to
the lesson videos, and also referring to videos and articles written online by
other people who experienced similiar issues to mine or had similiar experiences.

### Technologies Used to Complete Backend
python
django
Terminal
psql

### User Stories -API
As a user, id like to sign up
As a user, id like to sign in
As a user, id like to change password
As a user, id like to log out securly
As a user, id like to create a personal profile/post
As a user, id like to edit my post
As a user, id like to delete my post
As a user, id like to comment on others posts

### The following is the link to my ERD imgur
[ERD]()

### Unsolved Problems
I have yet to create a Comment model. I am also having a few issues communicating
with the back-end when it comes to creating ID's on the backend in order to
send them to the front-end to crud on created profiles.
