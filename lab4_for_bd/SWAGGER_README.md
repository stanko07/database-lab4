# Swagger API Documentation

## Installation

The `flasgger` library has been installed and configured for your Flask application.

```bash
pip install flasgger==0.9.7.1
```

## Configuration

Swagger has been configured in `app/__init__.py` with the following settings:

- **Swagger UI URL**: `http://localhost:5000/apidocs/`
- **API Spec URL**: `http://localhost:5000/apispec.json`

## API Endpoints Documentation

All route files in the `app/root/` directory have been updated with Swagger decorators using `@swag_from()`.

### Available API Groups:

1. **Candidates** - `/candidates` - Manage candidate information
2. **Companies** - `/company` - Manage company records
3. **Contact Persons** - `/contact_person` - Manage company contact persons
4. **Experience** - `/experience` - Manage candidate work experience
5. **Interviews** - `/interviews` - Manage interview schedules
6. **Interview Results** - `/interview_results` - Manage interview outcomes
7. **Projects** - `/projects` - Manage company projects
8. **Skills** - `/skills` - Manage skill definitions
9. **Vacancies** - `/vacancii` - Manage job vacancies
10. **Candidate Skills** - `/candidate_have_skills` - Manage candidate-skill relationships

## Usage

1. Start your Flask application:

   ```bash
   python app.py
   ```

2. Open your browser and navigate to:

   ```
   http://localhost:5000/apidocs/
   ```

3. You'll see an interactive Swagger UI with all your API endpoints organized by tags.

4. Each endpoint includes:
   - Request parameters and body schemas
   - Response codes and descriptions
   - Try-it-out functionality to test endpoints directly from the browser

## Features

- **Interactive Documentation**: Test API endpoints directly from the Swagger UI
- **Request/Response Schemas**: See exactly what data format is expected
- **HTTP Status Codes**: Clear indication of possible response codes
- **Organized by Tags**: Endpoints grouped by resource type for easy navigation
- **English Documentation**: All descriptions and summaries in English

## Example Request

To test an endpoint:

1. Click on any endpoint in Swagger UI
2. Click "Try it out"
3. Fill in the required parameters
4. Click "Execute"
5. View the response below

## Notes

- All documentation is in English
- Each CRUD operation (GET, POST, PUT, PATCH, DELETE) is documented
- Request body examples are provided for POST and PUT operations
- Path parameters are clearly marked as required
