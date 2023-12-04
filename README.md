<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/your_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Windows Event Log Ingestor</h3>

  <p align="center">
    Ingest Windows event logs into MongoDB and query them with a Gradio interface.
    <br />
    <a href="https://github.com/your_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/your_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/your_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/your_username/repo_name/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a project for ingesting Windows event logs into MongoDB and querying them through a Gradio interface. The Log Ingestor extracts logs from Windows event logs and stores them in MongoDB, while the Query Interface allows users to filter and query the stored logs with a user-friendly Gradio interface.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* https://www.gradio.app/
* https://www.mongodb.com/)
* https://github.com/wuxc/pywin32doc/blob/master/md/win32evtlog.md
* https://pymongo.readthedocs.io/en/stable/
* https://docs.python.org/3/library/tkinter.html


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
### Prerequisites

Ensure that you have the following prerequisites installed on your machine:

- [Python](https://www.python.org/downloads/) (V3.11)
- [MongoDB](https://www.mongodb.com/try/download/community) (for storing logs)

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/dyte-submissions/november-2023-hiring-HAWK1704
    ```

2. **Navigate to the project directory:**

    ```sh
    cd repo_name
    ```

3. **Create a virtual environment (optional but recommended):**

    ```sh
    python -m venv venv
    ```

4. **Activate the virtual environment:**
   - On Windows:
     ```sh
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

5. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

6. **Configure MongoDB:**
   - Install MongoDB and set it up according to your operating system.
   - Update MongoDB connection details in the `Log_Ingestor` and `Query_Interface` scripts.

7. **Run Log Ingestor(Open Log_Ingestor.py and replace 'localhost' and 'port' to your MongoDB Connector):**

    ```sh
    python Log_Ingestor.py
    ```

    This will start ingesting Windows event logs into MongoDB.

8. **Launch Query Interface(Open Query_Interface.py and replace 'localhost' and 'port' to your MongoDB Connector):**

    ```sh
    python Query_Interface.py
    ```

    Access the Gradio interface to query and filter the stored logs.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

###CONTACT

Om Prakash Singh

Email:thakur.omprakashsingh1704@gmail.com

project link:https://github.com/dyte-submissions/november-2023-hiring-HAWK1704
