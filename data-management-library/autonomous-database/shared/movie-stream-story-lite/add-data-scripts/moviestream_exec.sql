create or replace procedure moviestream_exec 
(
  sql_ddl in varchar2,
  raise_exception in boolean := false
  
) as 
begin
    -- Wrapper for execute immediate
    moviestream_write(sql_ddl);
    execute immediate sql_ddl;
    
    exception
      when others then
        if raise_exception then
            raise;
        else    
            moviestream_write(sqlerrm);
        end if;
    
end moviestream_exec;