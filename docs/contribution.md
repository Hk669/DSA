---
icon: material/alert-outline
---

# Contribution Guidelines

Thank you for considering contributing to DSA Solutions! Your contributions are highly valued and essential for improving our platform. Before submitting your contributions, please take a moment to review the guidelines below:

### Types of Contributions

- **Optimization**: While the existing solutions reflect the author's understanding, you're encouraged to optimize them further for efficiency.
- **Documentation Enhancement**: If you spot any inaccuracies, unclear explanations, or missing details in the documentation, feel free to enhance it.
- **New Solutions**: If you have solutions to problems not yet covered on the platform, you're welcome to submit them. Ensure they are well-explained and documented.

### How to Contribute

!!! tip "support"

    Before making any contributions, please consider starring the repository. Your support in starring the repository will greatly motivate and encourage me to continue learning and contributing more. Thank you for your support!

1. Fork the repository to your GitHub account.
2. Clone the forked repository to your local machine.
3. Create a new branch for your contributions: `git checkout -b my-contribution`
4. Make your desired changes or additions.
5. Ensure your code adheres to the existing style and formatting.
6. Test your changes locally if applicable.
7. Commit your changes: `git commit -m "Add my contribution"`
8. Push your changes to your forked repository: `git push origin my-contribution`
!!! warning

    Before making any contributions, please ensure that you follow the provided pull request template. The template serves as a guideline for submitting your changes in a structured manner, facilitating the review process. You can find the pull request template [here](https://github.com/Hk669/DSA/blob/main/.github/PULL_REQUEST_TEMPLATE.md). Your adherence to the template is greatly appreciated. Thank you for your cooperation!

 Create a pull request (PR) to the main repository's `main` branch, detailing the changes you've made and their significance.

### Use Docker

1. **Install Docker Desktop**: If you haven't already, install Docker Desktop on your local machine.
2. **Pull Docker Image**: Pull the Docker image from Docker Hub using the following command:
    ```sh
    docker pull hk669/dsadocs:latest
    ```
3. **Start Container**: Run the Docker container in detached mode and map port 8000 on your local machine to port 8000 inside the container:
    ```sh
    docker run -d -p 8000:8000 hk669/dsadocs:latest
    ```
4. **Edit Files**: Once the container is running, you can edit the files locally on your machine using your preferred code editor.
5. **Test Changes**: Verify your changes by accessing the documentation site at http://localhost:8000 in your web browser.
6. **Push Changes**: Once you're satisfied with your changes, commit them to your forked repository and push the changes to GitHub.

By using Docker, you can ensure a consistent development environment and easily share your contributions with others. Happy coding!


### Code Guidelines

- Follow consistent coding styles and naming conventions.
- Comment your code where necessary for clarity.
- Optimize solutions for efficiency while maintaining readability.
- Ensure your code is well-documented and easy to understand.

### Collaboration

Collaboration is key to our mission of continuous improvement. Feel free to discuss ideas [here](https://github.com/Hk669/DSA/discussions), suggest improvements, or seek assistance via issues or pull requests. Let's work together to make DSA Solutions an invaluable resource for students and enthusiasts alike!

Thank you for your contribution and dedication to advancing our understanding of data structures and algorithms. Happy coding!

!!! note

     By contributing to this project, you agree to license your work under the same license as the project itself.