function () {
    const tableRef = useRef(null);
    const wrapperRef = useRef(null);
    useEffect(() => {
      const grid = new gridjs.Grid({
        from: tableRef.current,
      }).render(wrapperRef.current);
    });
    return (
      <>
        <table ref={tableRef}>
  <table class = "table">
   <thead>
    <th>name</th>
    <th>address</th>
    <th>phone</th>
    <th>event</th>
    <th>email</th>
   </thead>
   
  {% for S in StudentSelect %}
    <tr>
      <td>{{ S[1] }}</td>
      <td>{{ S[2] }}</td>
      <td>{{ S[3] }}</td>
      <td>{{ S[4] }}</td>
      <td>{{ S[5] }}</td>
    </tr>
  {% endfor %}
</table></h6>  
</>
);
    }