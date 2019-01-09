from flask import request
from flask_restful import Resource
from models import db, Job, JobSchema

from .helper import *

job_list_schema = JobSchema(many=True)
job_schema = JobSchema()

# Job
# shows a single job
class JobResource(Resource):
    def get(self, jobID):
        return generic_get_single(Job, jobID, job_schema)

    # Delete Job
    def delete(self, jobID):
        job = Job.query.filter(Job.id == jobID).delete()
        db.session.commit()

        result = job_schema.dump(job).data

        return result, 204

# Job List
# - get to show a list of all jobs
# - post to add a new job
# - put to edit a existing job
# - delete to delete job
class JobListResource(Resource):
    # Get Jobs
    def get(self):
        # return generic_get_all(Job, job_list_schema)

        # TESTING:
        json_data = request.get_json(force=False)
        if not json_data:
            return generic_get_all(Job, job_list_schema)

        entry = Job.query.filter(Job.name.like("%"+json_data["name"]+"%"))
        entry = job_list_schema.dump(entry).data
        return entry, 200

    # New Job
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400

        # Validate and deserialize input
        print(json_data)
        job, errors = job_schema.load(json_data)
        if errors:
            return errors, 422

        db.session.add(job)
        db.session.commit()

        result = job_schema.dump(job).data

        return result, 201


    # Edit Job
    def put(self):
        json_data = request.get_json(force=True)
        print(json_data)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = job_schema.load(json_data)
        if errors:
            print(errors)
            return errors, 422

        job = Job.query.filter(Job.id == data.id).first()
        job.updateFromSchema(data)
        db.session.commit()

        result = job_schema.dump(job).data

        return result, 201
