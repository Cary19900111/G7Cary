class StringJoin(object):
    def __init__(self,str1,str2):
        self.str1 = str1
        self.str2 = str2
        self.result = ""
    def by_add(self):
        self.result = self.str1+self.str2
    def by_join_method(self):
        str_list = [self.str1,self.str2]
        self.result = ''.join(str_list)
    def by_format(self):
        self.result = '{} {}'.format(self.str1,self.str2)
    def by_operation(self):
        self.result = '%s %s'%(self.str1,self.str2)
    # def by_multi_line(self):
    #     s = (
    #         'Hello'
    #         ' '
    #         'World'
    #         '!'
    #     )
    #     print(s)
    def by_template(self):
        from string import Template
        s = Template('${s1} ${s2}')
        self.result = s.safe_substitute(s1=self.str1,s2=self.str2)
    def by_F_strings(self):
        self.result = f'{self.str2} {self.str2}'
    def reset_result(self):
        self.result=""

if __name__=='__main__':
    sj = StringJoin("hello","world")
    sj.by_add()
    print(sj.result)
