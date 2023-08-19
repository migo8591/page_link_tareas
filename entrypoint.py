from app import create_app

myApp = create_app()

if __name__ == '__main__':
    myApp.run(port=6015, debug= True) 