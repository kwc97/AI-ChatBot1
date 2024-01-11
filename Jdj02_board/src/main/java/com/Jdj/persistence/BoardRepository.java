package com.Jdj.persistence;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.query.Param;
import org.springframework.transaction.annotation.Transactional;

import com.Jdj.domain.Board;

public interface BoardRepository extends CrudRepository<Board, Long>{
	
	// 클래스, 메서드 모두에 @Transactional  애너테이션을 선언하면 
	// 메서드레벨의 @Transactional선언이 우선 적용이 된다.
	// @Transactional으로 선언된 메서드는 메서드가 포함된 작업중에 하나라도 실행이 실패할 경우
	// 전체작업이 취소된다.
	// @Modifying 애너테이션은 @Query 애너테이션에서 작성된 쿼리에서 조회를 제외한
	// 데이트의 변경(insert, delete, update)이 있는 쿼리를 사용할 경우에 선언해야 한다. 
	@Modifying      // @Query의 sql이 insert/delete/update
	@Transactional  // commit, rollback
	@Query("update Board b set b.cnt = b.cnt + 1 where b.seq = :seq")
	int updateReadCount(@Param("seq") Long seq);
	
	@Modifying     
	@Transactional 
	@Query("update Board b set b.board_ref = b.seq, b.board_lev=:lev, b.board_seq=:_seq where b.seq = :seq")
	void updateLastSeq(@Param("lev") Long i, @Param("_seq") Long j, @Param("seq") Long seq);
	
	Page<Board> findByTitleContaining(String Title, Pageable pageable);
	Page<Board> findByWriterContaining(String Writer, Pageable pageable);
	Page<Board> findByContentContaining(String Content, Pageable pageable);
}
