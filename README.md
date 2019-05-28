#evaluate kvmtop

## A: measurements inside VM are same as outside

    Monitoring inside with TICK stack, and outside with kvmtop.

    Four artificial workloads: 
    
    | name | tool |
    | --- | --- |
    | cpu | cpu stress |
    | disk read | dd read |
    | disk write | dd write |
    | net | wget download |


```
    /bin/bash -c 'for i in {1..20};do echo "start run $i"; cpu-stress-random 60 && sleep 30 ; done'
    
    /bin/bash -c 'cpu-stress-random 60 && sleep 30 && disk-read 5000 && sleep 30 && disk-write 5000 && sleep 30 && net-read && sleep 30'
```


## B: detection of bottlenecks works (cpu, disk i/o, network i/o)