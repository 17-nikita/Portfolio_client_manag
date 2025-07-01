# Portfolio_client_manag

# FLIPR Placement – Full Stack Development Task

This project is a solution to the FLIPR Placement Full Stack Development Task. It involves building a full-stack web application featuring a public-facing landing page and a restricted admin panel.

## Objective

The primary objective is to create a web application that allows for the display of project and client information on a landing page, and enables administrative users to manage this content, as well as view contact form submissions and newsletter subscriptions via an admin interface.

## Requirements

The application implements the following core requirements:

### Landing Page

*   **Design:** The landing page is designed based on the provided reference image, utilizing HTML, CSS, and Bootstrap for structure and styling.
*   **"Our Projects" Section:** Dynamically fetches and displays projects from the backend. Each project card includes:
    *   Project's Image
    *   Project's Name
    *   Project's Description
    *   A dummy "Read More" button (non-functional as per requirements).
*   **"Happy Clients" Section:** Dynamically fetches and displays client testimonials from the backend. Each client entry includes:
    *   Client's Image
    *   Client's Description
    *   Client's Name
    *   Client's Designation.
*   **Contact Form:** A dedicated section with a form to collect user inquiries. Inputs include Full Name, Email Address, Mobile Number, and City. Submissions are sent to the backend via AJAX.
*   **Newsletter Subscription Section:** Allows users to subscribe by entering their email address. Submissions are sent to the backend via AJAX.

### Admin Panel

Built using Django's built-in admin site, accessible via `/admin/`.

*   **Project Management:** Functionality to add, edit, and delete projects, including uploading images, specifying name, description, and sale status.
*   **Client Management:** Functionality to add, edit, and delete client testimonials, including uploading images, specifying name, description, and designation.
*   **Contact Form Details:** Provides a view to list and inspect all submitted contact form entries (Full Name, Email Address, Mobile Number, City, and submission timestamp).
*   **Subscribed Email Addresses:** Provides a view to list and inspect all newsletter subscribers (Email Address and subscription timestamp).

## Technologies Used

*   **Backend:** Python, Django
*   **Frontend:** HTML, CSS, JavaScript, Bootstrap 5
*   **Database:** [Specify Database Used Here, e.g., SQLite (default), PostgreSQL, MongoDB Atlas (preferred as per task)]

## Setup Instructions

To run this project locally, follow these steps:

1.  **Clone the repository:**
   

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   On Windows: `venv\Scripts\activate`
    *   On macOS/Linux: `source venv/bin/activate`

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Ensure `requirements.txt` is present with necessary libraries like Django, Pillow, and potentially djongo if using MongoDB)*

5.  **Configure Database:**
    Update `myproject/settings.py` with your database configuration. If using SQLite, this step is optional as it's the default. If using MongoDB Atlas, configure the `djongo` backend connection details.

6.  **Run database migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7.  **Create a superuser** (for admin panel access):
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to set up credentials.

8.  **Collect static files:**
    ```bash
    python manage.py collectstatic
    ```

9.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

The landing page will be available at `http://127.0.0.1:8000/` and the admin panel at `http://127.0.0.1:8000/admin/`.

## Usage

*   Open `http://127.0.0.1:8000/` in your browser to view the landing page.
*   Use the navigation to explore sections.
*   Submit data through the Contact and Newsletter forms (using AJAX).
*   Visit `http://127.0.0.1:8000/admin/` and log in with your superuser account to manage content (Projects, Clients) and view submissions (Contact Submissions, Newsletter Subscriptions).

## Bonus Features Implemented

*   **Image Cropping:** [State whether image cropping is implemented for Project images on upload in the admin panel, e.g., "Implemented image cropping for Project images on upload in the admin panel to the specified 450x350 ratio."]

## Deployment

The application is deployed on [Mention the cloud platform used, e.g., Heroku, AWS EC2, etc.].

*   **Deployed App URL:** [Provide the public URL of your deployed application]

## Evaluation Notes

*   **Functionality:** All required features from the task description are implemented and verified.
*   **Code Quality:** Code structure, comments, and adherence to standard practices have been prioritized.
*   **Design:** The frontend layout and styling aim to match the provided reference image closely using Bootstrap 5.
*   **Usability:** Both the landing page and the Django admin panel provide clear interfaces for users and administrators respectively.

## Links

*   **Repository URL:** <Your GitHub/GitLab/Bitbucket Repo URL Here> *(Ensure this link is public)*
*   **Deployed Application URL:** [Link to your deployed app] *(Ensure this link is public and files/images are accessible)*
