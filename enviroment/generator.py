# -*- coding: utf-8 -*-
import json

data = [] # data config to generate forms


form = """
    <form class="form-horizontal">

      <div class="form-group">
        <label for="inputEmail3" class="col-sm-2 control-label">Email</label>
        <div class="col-sm-10">
          <input type="email" class="form-control" id="inputEmail3" placeholder="Email">
        </div>
      </div>

      <div class="form-group">
        <label for="inputPassword3" class="col-sm-2 control-label">Password</label>
        <div class="col-sm-10">
          <input type="password" class="form-control" id="inputPassword3" placeholder="Password">
        </div>
      </div>
      <div class="form-group">
        <div class="col-sm-offset-2 col-sm-10">
          <div class="checkbox">
            <label>
              <input type="checkbox"> Remember me
            </label>
          </div>
        </div>
      </div>
      <div class="form-group">
        <div class="col-sm-offset-2 col-sm-10">
          <button type="submit" class="btn btn-default">Sign in</button>
        </div>
      </div>
    </form>
     """ 

form_base = """
                 <form class="form-horizontal">
            """

form_end = "</form>"



def load_json(file_path):
    """

	Generate the json config to evaluate and create de forms Bootstrap 3

    """
    file_config = open(file_path, 'r')
   
    
    my_dict = eval(file_config.read())

    print my_dict['fields']

    if( len(my_dict['fields']) > 0 ): 
        form_new = form_base
        for field in  my_dict['fields'] :

            print "s"
            form_new += create_input(field['type'],field['id'],field['name'],field['value'],field['maxlength'],field['label'])

        form_new += form_end
        print form_new


print "************************************************************************************************************************************************************************"
print "********************************************************* Readind config file ******************************************************************************************"


def create_input(typeField,id_,name,value,maxlength,label):
    input = """
            <div class="form-group">
            <label for='"""+str(name)+"""' class="col-sm-2 control-label">"""+str(label)+"""</label>
            <div class="col-sm-10">
              <input type='"""+str(typeField)+"""'     maxlength='"""+str(maxlength)+"""'       class="form-control" id='"""+str(id_)+"""' placeholder='Ingrese """+str(label)+"""'>
            </div>
          </div>

        """
    return input 


def main():
    
    load_json('file.py')

if __name__ == '__main__':     # if the function is the main function ...
    main() # 

