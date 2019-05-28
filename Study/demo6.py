# Test os
import os
# Test pickle 永久储存为二进制文件
import pickle
print(os.getcwd())
# os.system('calc')
os.system('start cmd')

testlist=[1,2,3,4,5,6]
pickle_file=open('E:\\PythonSave\\Study\\test_pickle.pkl','wb')
pickle.dump(testlist,pickle_file)
pickle_file.close()
pickle_file=open('test_pickle.pkl','rb')
testlist2=pickle.load(pickle_file)
print(testlist2)
pickle_file.close()
