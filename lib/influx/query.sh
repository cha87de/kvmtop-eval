
function influx_query(){
    query="$1"

    echo "$query"
    influx \
        -username $INFLUX_USER \
        -password $INFLUX_PASS \
        -host $INFLUX_HOST  \
        -database "kvmtop" \
        -execute "$query" \
        -format csv
}
