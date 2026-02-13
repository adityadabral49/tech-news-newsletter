📰 Daily Tech News Newsletter (AWS Lambda + EventBridge + SES)

This serverless, AWS-based project automatically retrieves the latest technology news headlines and dispatches a daily newsletter via email. The solution leverages AWS Lambda, Amazon SES, and EventBridge Scheduler.

🚀 Project Overview

This project provides a fully automated Daily Tech Newsletter, delivered to a verified email address.

Workflow:

AWS Lambda fetches the latest technology news from NewsAPI.
The news is formatted into a clean newsletter structure.
AWS SES is used to send the newsletter email.
AWS EventBridge Scheduler automatically triggers the Lambda function on a daily basis.

🛠️ Tech Stack

Python 3.12
AWS Lambda
AWS EventBridge Scheduler
AWS SES (Simple Email Service)
NewsAPI
requests library

📌 Features

Fetches the latest technology news (Top Headlines)
Creates a formatted newsletter, including title, source, and link.
Sends emails via AWS SES.
Fully automated daily scheduling via EventBridge Scheduler.
Serverless architecture (no server required).
Uses environment variables for secure configuration.

📂 Project Structure
news-newsletter/
│
├── lambda_function.py          # Main Lambda handler
├── fetch_news.py               # Fetches news from NewsAPI
├── newsletter_email.py         # Sends newsletter email using AWS SES
├── requirements.txt            # Python dependencies
└── README.md                   # Documentation

⚙️ How It Works (Architecture)
AWS Flow:

EventBridge Scheduler → AWS Lambda → NewsAPI → AWS SES → Email Inbox

Here's an enhanced version of the provided text:

Step-by-Step:

*   EventBridge Scheduler executes daily (rate(1 day)).
*   It triggers the Lambda function.
*   The Lambda function then invokes the NewsAPI.
*   The Lambda function formats the top headlines.
*   The Lambda function sends an email via SES.
*   The email is delivered to the designated recipient's inbox.

🔑 Required Environment Variables

These variables must be configured within AWS Lambda under Configuration → Environment Variables:

| Variable Name   | Description                                         |
| :-------------- | :-------------------------------------------------- |
| `NEWS_API_KEY`  | API key obtained from NewsAPI                       |
| `SENDER_EMAIL`  | Verified SES sender email address                   |
| `RECEIVER_EMAIL` | Verified SES recipient email address                |
| `AWS_REGION`    | The AWS region (e.g., `ap-south-1`)                 |

Example:

```
NEWS_API_KEY=your_news_api_key_here
SENDER_EMAIL=your_verified_email@gmail.com
RECEIVER_EMAIL=receiver_email@gmail.com
AWS_REGION=ap-south-1
```

🧾 Setup Instructions (Local Setup)

1.  Clone the Repository:

    ```bash
    git clone https://github.com/adityadabral49/tech-news-newsletter.git
    cd tech-news-newsletter
    ```

2.  Create a Virtual Environment:

    ```bash
    python -m venv venv
    ```

    Activate the venv:

    *   Windows:

        ```bash
        venv\Scripts\activate
        ```

        ```

3️⃣ Install Dependencies
pip install -r requirements.txt

🧪 Run Locally (Testing)

To test the application locally, you can execute the following commands:

*   `python fetch_news.py`: This script is designed to retrieve and process the latest tech news.
*   `python newsletter_email.py`: This script is responsible for sending out the compiled tech news newsletter via email.

☁️ AWS Deployment Steps

Here's a breakdown of how to deploy the application to AWS:

Step 1: Create Lambda Function

*   Navigate to the AWS Lambda service.
*   Click on "Create Function."
*   Configure the runtime environment to Python 3.12.
*   Upload a zip file that contains the application code and its necessary dependencies.

Step 2: Configure Handler

*   Set the handler function to `lambda_function.lambda_handler`. This specifies which function within your code should be executed when the Lambda function is triggered.

Step 3: Add Environment Variables

*   Go to the Lambda function's configuration.
*   Under "Environment Variables," add the following:

    *   `NEWS_API_KEY`: Your API key for accessing the news API.
    *   `SENDER_EMAIL`: The email address from which the newsletter will be sent.
    *   `RECEIVER_EMAIL`: The recipient's email address.
    *   `AWS_REGION`: The AWS region where your resources are deployed.

Step 4: Setup SES (Simple Email Service)

*   Go to the AWS SES service.
*   Verify both the sender and receiver email addresses. If you are in the SES sandbox, you may need to verify the receiver email.
*   Optionally, request to move out of the sandbox to send emails to unverified recipients.

Step 5: Create EventBridge Scheduler

*   Go to the AWS EventBridge Scheduler.
*   Create a new schedule.
*   Set the `Rate expression` to `rate(1 day)` to trigger the Lambda function daily.
*   Set the `Target` as the Lambda function you created.

This setup ensures that the Lambda function, and therefore your tech news newsletter, runs automatically every day.
🔥 Daily Tech Newsletter 🔥
Headline Title
Source: BBC News
Link: https://example.com/news

Headline Title
Source: The Verge
Link: https://example.com/news

**AWS Services Used**
*   AWS Lambda
    *   Runs the Python code serverlessly.
*   Amazon SES
    *   Sends the newsletter email.
*   Amazon EventBridge Scheduler
    *   Triggers Lambda automatically daily.
*   CloudWatch Logs
    *   Stores logs of Lambda execution.

**Learnings from This Project**
*   Serverless automation using AWS Lambda
*   Event-driven scheduling with EventBridge Scheduler
*   Email automation using Amazon SES
*   Environment variables & secure config handling
*   API integration with Python requests
*   AWS CloudWatch logging for debugging

**Future Enhancements**
*   Add support for multiple subscribers
*   Store subscriber list in DynamoDB
*   Add HTML formatted newsletter template
*   Add categories like sports, finance, business
*   Add error handling & retry mechanism
*   Deploy using Terraform / CloudFormation
