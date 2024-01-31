
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movies, Actors
from dotenv import load_dotenv

load_dotenv()

class CapstoneTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.db = SQLAlchemy(self.app)
        self.client = self.app.test_client
        self.database_path = os.environ.get("DATABASE_PATH")
        # self.unauthorized_jwt = os.environ['INVALID_TOKEN']
        self.producer_jwt = os.environ["EXECUTIVE_PRODUCER_JWT"]
        # self.producer_jwt = os.environ['PRODUCER_TOKEN']
        setup_db(self.app, self.database_path)

    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def testGetMovies(self):
        authHeader = {'Authorization': f'Bearer {self.producer_jwt}'}
        res=self.client().get('/movies', headers=authHeader)
        data=json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data!=None)

    def testGetMovies_error(self):
        res = self.client().get('/movies')  #without authToken
        data=json.loads(res.data)
        self.assertEqual(res.status_code,401)

    def testGetActors(self):
        authHeader = {'Authorization': f'Bearer {self.producer_jwt}'}
        res = self.client().get('/actors',headers=authHeader)
        data=json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data!=None)

    def testGetActors_error(self):
        res = self.client().get('/actors')
        data=json.loads(res.data)
        self.assertEqual(res.status_code,401)

    def testDeleteMovie(self):
        authHeader = {'Authorization': f'Bearer {self.producer_jwt}'}
        newMovie=Movies(
            title="What is your name",
            release_date="15th March 2024"
        )
        self.db.session.add(newMovie)
        self.db.session.commit()
        id=newMovie.id
        res = self.client().delete('/movies/'+str(id),headers=authHeader)
        self.assertEqual(res.status_code,200)
        self.assertEqual(res.data.decode(),"DELETED")

    def testDeleteMovie_error(self):
        newMovie=Movies(
            title="What is your name",
            release_date="15th March 2024"
        )
        self.db.session.add(newMovie)
        self.db.session.commit()
        id=newMovie.id
        res = self.client().delete('/movies/'+str(id))
        self.assertEqual(res.status_code,401)
        
    def testDeleteActor(self):
        authHeader = {'Authorization': f'Bearer {self.producer_jwt}'}
        newActor=Actors(
            name="Preeti",
            age="22",
            gender="Female"
        )
        self.db.session.add(newActor)
        self.db.session.commit()
        id=newActor.id
        res = self.client().delete('/actors/'+str(id),headers=authHeader)
        self.assertEqual(res.status_code,200)
        self.assertEqual(res.data.decode(),"DELETED")

    def testDeleteActor_error(self):
        authHeader = {'Authorization': f'Bearer {self.producer_jwt}'}
        res = self.client().delete('/movies/100',headers=authHeader)
        self.assertEqual(res.status_code,404)
       
    def testPostMovie(self):
        authHeader = {'Authorization': f'Bearer {self.producer_jwt}'}
        newMovie={
            "title":"What is your name",
            "release_date":"15th March 2024"
        }
        res = self.client().post('/movies',json=newMovie,headers=authHeader)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)

    def testPostMovie_error(self):
        authHeader = {'Authorization': f'Bearer {self.producer_jwt}'}
        newMovie={
            "title":"What is your name"
        }
        res = self.client().post('/movies',json=newMovie,headers=authHeader)
        self.assertEqual(res.status_code, 422)

    def testPostActor(self):
        authHeader = {'Authorization': f'Bearer {self.producer_jwt}'}
        newActor={
            "name":"Preeti",
            "age":"22",
            "gender":"Female"
        }
        res = self.client().post('/actors',json=newActor,headers=authHeader)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)

    def testPostActor_error(self):
        authHeader = {'Authorization': f'Bearer {self.producer_jwt}'}
        newActor={
            "name":"name"
        }
        res = self.client().post('/actors',json=newActor,headers=authHeader)
        self.assertEqual(res.status_code, 422)

    def testPatchMovie(self):
        authHeader = {'Authorization': f'Bearer {self.producer_jwt}'}
        newMovie={
            "title":"test edit",
            "release_date":"15th March 2024"
        }
        res = self.client().patch('/movies/2',json=newMovie,headers=authHeader)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['title'],newMovie.get('title'))

    def testPatchMovie_error(self):
        authHeader = {'Authorization': f'Bearer {self.producer_jwt}'}
        newMovie={
            "title":"test edit 1"
        }
        res = self.client().patch('/movies/2',json=newMovie,headers=authHeader)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)

    def testPatchActor(self):
        authHeader = {'Authorization': f'Bearer {self.producer_jwt}'}
        newMovie={
            "name":"test",
            "age":"15",
            "gender":"Female"
        }
        res = self.client().patch('/actors/2',json=newMovie,headers=authHeader)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['name'],newMovie.get('name'))

    def testPatchActor_error(self):
        authHeader = {'Authorization': f'Bearer {self.producer_jwt}'}
        newMovie={
            "name":"test edit 1"
        }
        res = self.client().patch('/actors/2',json=newMovie,headers=authHeader)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)

    def testGetMovie(self):
            authHeader = {'Authorization': f'Bearer {self.producer_jwt}'}
            res=self.client().get('/movies/2', headers=authHeader)
            data=json.loads(res.data)
            self.assertEqual(res.status_code,200)
            self.assertTrue(data!=None)

    def testGetMovie_error(self):
        res = self.client().get('/movies/2')  #without authToken
        data=json.loads(res.data)
        self.assertEqual(res.status_code,401)

    def testGetActor(self):
        authHeader = {'Authorization': f'Bearer {self.producer_jwt}'}
        res = self.client().get('/actors/2',headers=authHeader)
        data=json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data!=None)

    def testGetActor_error(self):
        res = self.client().get('/actors/2')
        data=json.loads(res.data)
        self.assertEqual(res.status_code,401)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()