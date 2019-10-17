# Current Features

-Decent HTML/CSS (would like someone to review it)<br>
-Event system that supports file uploads (event system is like a linear calendar)<br>
-System in DB for text pages that uses django-precise-bbcode for format<br>
(https://django-precise-bbcode.readthedocs.io/en/stable/index.html)

# Run

Do "pip install django-precise-bbcode" before running.
The BBCode module is used for rendering content from the database.  This may or may not go away.<br>

To run: "python manage.py runserver"<br>
This will run the server on http://127.0.0.1:8000 by default.  Or, specify a custom host:port after runserver in the command.<br>

Or, visit the current build at https://counseling.ptgough.com (Please let Patrick know if it is broken so he can reboot the ptgough.com server) (502 Bad Gateway = broken).<br><br>

# Website Structure

There are currently three models in the database as deinfed in core/models.py.<br><br>

TextPage is a container that stores text to render on a page in the BBCode format.  The model has fields for text and a field for the priority.  Priority represents the order the instance is displayed in the sidebar.<br>
The curent order is in line with the previous RC's request.<br><br>

Event is for announcements.  Events contain a datestamp and text.  They are displayed in a linear fashion in the events link.<br><br>

File is for uploading user files.  Currently, events can ForeignKey into files to render them as attachments.<br>
However, as the new department is ONLY working in Google, file uploads are no longer necessary.<br><br>

Currently, there is no framework for announcements, but the Twitter feed is showing.<br><br>

The HTML files all use the Django include statement to "include" the header and sidebar files.  This statement injects the HTML from the header into the HTML for the other files.  This system makes it easier to change the header without manually updating the rest of the site.<br><br>

To see all BBCode tags, go here https://django-precise-bbcode.readthedocs.io/en/stable/basic_reference/builtin_bbcodes.html.
