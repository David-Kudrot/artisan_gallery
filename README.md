# Artisan Gallery

Artisan Gallery is a platform for artists to showcase their artworks and connect with art enthusiasts. This project provides a set of API endpoints for artists to manage their profiles, artworks, and interactions within the platform.

## Features

- **User Authentication:** Artists can register, log in, and manage their profiles securely.
- **Profile Management:** Users can view, create, and update their profiles.
- **Password Management:** Artists can change their passwords and request password resets.
- **Artwork Management:** Artists can upload, edit, and delete their artworks.
- **Artwork Display:** Users can view all artworks or access specific artworks via API endpoints.
- **Authorization:** Access to protected endpoints requires authentication via bearer tokens.

## API Endpoints

- `/api/artist/register/`: Register a new artist.
- `/api/artist/login/`: Log in an existing artist.
- `/api/artist/profile/`: View artist profile data.
- `/api/artist/my-profile/`: Create or update artist profile.
- `/api/artist/change-password/`: Change artist password.
- `/api/artist/password-reset-email/`: Send password reset email.
- `/api/artist/reset-password/{uid}/{token}/`: Reset password via email link.
- `/api/art/artworks/`: View all artworks.
- `/api/art/artworks/{id}/`: View, edit, or delete a specific artwork.

## Usage

1. Clone the repository: `git clone <repository_url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `python manage.py runserver`

Make sure to set up your database configuration in `settings.py` before running the server.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or feedback, please contact [davidkudrot@gmail.com](mailto:davidkudrot@gmail.com).
