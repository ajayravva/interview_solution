### Interview Solution

Frappe Interview Assignment

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app interview_solution
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/interview_solution
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit


# Interview Solution – Frappe Assignment

This repository contains the solution for the Frappe developer interview assignment.

## Setup Instructions

1. Install Frappe Bench

bench init frappe-bench
cd frappe-bench

2. Create a new site

bench new-site site1.local

3. Get the custom app

bench get-app https://github.com/ajayravva/interview_solution.git

4. Install the app

bench --site site1.local install-app interview_solution

5. Start the server

bench start

Open in browser:
http://localhost:8000
