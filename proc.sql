create proc datve
@makh int,
@mave int,
@trangthaitt int,
as
declare
@trangthai bit, 
@ngaytochuc bit,
begin transaction
    if not exists (select mave 
                    from vebuffet 
                    where @mave = mave)
    	begin
		rollback tran
		return
	end

    if not exists (select makh from khachhang where @makh = makh)
    	begin
		rollback tran
		return
	end

    select @trangthai = trangthai 
        from vebuffet 
        where @mave = mave
    if (@trangthai = 1)
    begin
        raiserror("ve da duoc dat",10,1)
        rollback tran
        return
    end
    select @ngaytochuc = ngaytochuc from vebuffet
    where @mave = mave
    if(@ngaytochuc >= now() )
    begin
        raiserror("ngay to chuc da qua",10,1)
		rollback tran
		return
	end
    update vebuffet set trangthai = 1 where @mave = mave
    if(@@error <> 0)
	begin
		rollback tran
		return
	end
    insert into quanlydatve values( @mave, now(), @makh, gettime() , trangthai = 0)
    if(@@error <> 0)
	begin
		rollback tran
		return
	end
    commit tran


