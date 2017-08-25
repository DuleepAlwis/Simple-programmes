def balancedparan(e):
    import stack
    a=stack.stack()
    d={'{':'}','[':']','(':')','/*':'*/'}
    for i in e:
        if i in d.keys():
            a.push(i)
        elif i in d.values():
            if a.isempty()==True:
                print("ERROR...Unbalanced...")
                return
            else:
                b=a.pop()
                if d[b]==i:
                    pass
                else:
                    print("Error...Unbalanced.....")
                    return
        else:
            pass

    if a.isempty()==True:
        print("OK.....Balanced...")
    else:
        print("Error.....Unbalanced......")



c='y'
while c=='y':
    q=input("Enter:")
    balancedparan(q)
    c=input("Continue(y/n):")

        
