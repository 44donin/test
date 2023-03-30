{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8e5083be",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import modules\n",
    "import smtplib, ssl\n",
    "## email.mime subclasses\n",
    "from email.mime.multipart import MIMEMultipart\n",
    "from email.mime.text import MIMEText\n",
    "### Add new subclass for adding attachments\n",
    "##############################################################\n",
    "from email.mime.application import MIMEApplication\n",
    "##############################################################\n",
    "## The pandas library is only for generating the current date, which is not necessary for sending emails\n",
    "import pandas as pd\n",
    "\n",
    "\n",
    "#html = open(\"/home/ubuntu/PRODUCTION/geogames/pipeline.html\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e3c52605",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2ff16d40",
   "metadata": {},
   "outputs": [],
   "source": [
    "def attach_file_to_email(email_message, filename):\n",
    "    # Open the attachment file for reading in binary mode, and make it a MIMEApplication class\n",
    "    with open(filename, \"rb\") as f:\n",
    "        file_attachment = MIMEApplication(f.read())\n",
    "    # Add header/name to the attachments    \n",
    "    file_attachment.add_header(\n",
    "        \"Content-Disposition\",\n",
    "        f\"attachment; filename= {filename}\",\n",
    "    )\n",
    "    # Attach the file to the message\n",
    "    email_message.attach(file_attachment)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "61f3be64",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(221, b'2.0.0 Service closing transmission channel')"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "email_from = 'donotreply@lognormal.io'\n",
    "password = 'Sag73665'\n",
    "email_to = 'saiteja.reddy@lognormal.io'\n",
    "\n",
    "# Generate today's date to be included in the email Subject\n",
    "date_str = pd.Timestamp.today().strftime('%Y-%m-%d')\n",
    "\n",
    "# Create a MIMEMultipart class, and set up the From, To, Subject fields\n",
    "email_message = MIMEMultipart()\n",
    "email_message['From'] = email_from\n",
    "email_message['To'] = email_to\n",
    "email_message['Subject'] = f'Report email - {\"testmail\"}'\n",
    "\n",
    "# Attach the html doc defined earlier, as a MIMEText html content type to the MIME message\n",
    "#email_message.attach(MIMEText(html.read(), \"html\"))\n",
    "#email_message.attach(MIMEText(body, \"html\"))\n",
    "\n",
    "# Attach more (documents)\n",
    "##############################################################\n",
    "#attach_file_to_email(email_message, attachement)\n",
    "#attach_file_to_email(email_message, 'excel_report.xlsx')\n",
    "#attach_file_to_email(email_message, 'fpdf_pdf_report.pdf')\n",
    "##############################################################\n",
    "# Convert it as a string\n",
    "email_string = email_message.as_string()\n",
    "\n",
    "\n",
    "server = smtplib.SMTP('smtp.outlook.com',587)\n",
    "server.starttls()\n",
    "server.login('donotreply@lognormal.io', \"Sag73665\")\n",
    "server.sendmail(email_from, email_to, email_string)\n",
    "server.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "849472b5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb67ab42",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8aac1888",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.2"
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
