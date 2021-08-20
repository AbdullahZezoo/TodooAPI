# TodooAPI

### Requirements
- Python 3
- Mysql
- Docker

### Install & Run
- Docker-compose build
- Docker-compose up

### API Documentation
- API Documenation with Swagger in the default url /.
- API Documentation with Redoc /redoc.
- /tasks    -- Get, POST, DELETE, PUT task.
- /finish_task/<id>   -- finish task by id or /tasks/<id>  Method=PUT and Update task {'status': 'finished'}
- /filter_tasks/<type>  -- Get tasks by type, type is finished or unfinished.
