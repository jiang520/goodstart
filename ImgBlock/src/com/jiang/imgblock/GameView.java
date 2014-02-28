package com.jiang.imgblock;

import java.util.Random;

import android.app.AlertDialog;
import android.app.AlertDialog.*;
import android.content.Context;
import android.content.DialogInterface;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Point;
import android.graphics.Rect;
import android.graphics.drawable.BitmapDrawable;
import android.util.Log;
import android.view.View;
import android.widget.Toast;


enum GAME_STATUS{
	STATE_PREVIEW,
	PLAYING
}

public class GameView extends View {


	public GameView(Context context) {
		super(context);
		this.setImage(R.drawable.img0);
		this.setLevel(3);		
		this.mStatus = GAME_STATUS.PLAYING;
	}

	@Override
	protected void onDraw(Canvas canvas) {
		
		Paint paint = new Paint();
		paint.setColor(Color.BLUE);
		//canvas.drawRect(new Rect(0, 100, 299,300), paint);
		//draw bitmap...
		if(this.mBmp == null) return;
		Bitmap bmp = this.mBmp;
		if(mStatus!=GAME_STATUS.PLAYING){
			Rect src = new Rect(0, 0, bmp.getWidth(), bmp.getHeight());
			Rect dst = new Rect(0, 0, this.getWidth(), this.getHeight());
			canvas.drawBitmap(bmp,src, dst, paint);
			return;			
		}
		for(int i=0; i<this.mArrayPos.length; i++)
		{
			int x, y;
			int nSrcPos = this.mArrayPos[i];
			if(nSrcPos < 0) continue;
			x = nSrcPos%mLevel;
			y = nSrcPos/mLevel;
			Rect src = new Rect(x*bmp.getWidth()/mLevel, y*bmp.getHeight()/mLevel, 
					(x+1)*bmp.getWidth()/mLevel, (y+1)*bmp.getHeight()/mLevel);
			
			int nDstPos = i;
			x = nDstPos%mLevel;
			y = nDstPos/mLevel;
			Rect dst = new Rect(x*canvas.getWidth()/mLevel, y*canvas.getHeight()/mLevel, 
					(x+1)*canvas.getWidth()/mLevel, (y+1)*canvas.getHeight()/mLevel);
			canvas.drawBitmap(this.mBmp, src, dst, paint);		
			paint.setTextSize(40);
			//canvas.drawText(i+"-"+mArrayPos[i], dst.left+10, dst.top+20, paint);
		}
		paint.setColor(Color.RED);
		//draw grid
		for(int i=1; i<this.mLevel; i++)
			canvas.drawLine(canvas.getWidth()*i/mLevel, 0, canvas.getWidth()*i/mLevel, canvas.getHeight(), paint);
		for(int i=1; i<this.mLevel; i++)
			canvas.drawLine(0, canvas.getHeight()*i/mLevel, canvas.getWidth(), canvas.getHeight()*i/mLevel, paint);
		super.onDraw(canvas);
	}
	
	public void setImage(int id){
		this.mBmp = ((BitmapDrawable)getResources().getDrawable(id)).getBitmap();
		
		this.invalidate();
	}
	//set game level
	public void setLevel(int nLevel){
		if(nLevel<3 || nLevel>6) return;
		this.mArrayPos = new int[nLevel*nLevel];
		this.mLevel = nLevel;
		for(int i=0; i<nLevel*nLevel; i++)
			this.mArrayPos[i]=i;
		this.mArrayPos[mLevel*mLevel-1]=-1;
		this.disorderBlocks();
	}
	public void restart(){
		disorderBlocks();
		this.mStatus = GAME_STATUS.PLAYING;
		this.invalidate();
	}
	
	protected void disorderBlocks()
	{
		int nBlankPos = getBlankPos();
		for(int i=0; i<mLevel*50; i++)
		{
			Random r = new Random(System.currentTimeMillis());
			int n = Math.abs(r.nextInt())%4;
			int nDst = nBlankPos;
			switch(n)
			{
			case 0: if(nBlankPos-1 >= 0) nDst = nBlankPos-1;break;
			case 1: if(nBlankPos-mLevel >= 0) nDst = nBlankPos-mLevel;break;
			case 2: if(nBlankPos+1 <mLevel*mLevel) nDst = nBlankPos+1;break;
			case 3:if(nBlankPos+mLevel < mLevel*mLevel) nDst = nBlankPos+mLevel;break;
			}
			if(nDst==nBlankPos) continue;
			Log.i("info--------", "swith "+nDst+"and "+nBlankPos);
			mArrayPos[nBlankPos]=mArrayPos[nDst];
			mArrayPos[nDst]=-1;
			nBlankPos = nDst;
		}
	}
	//check is game over;
	public boolean isGameOver(){
		for(int i=0; i<mArrayPos.length-1; i++){
			if(mArrayPos[i]!=i)
				return false;
		}
		return true;
	}
	//
	protected int getBlankPos(){
		int nBlankPos = -1;
		for(int i=0; i<mArrayPos.length; i++){
			if(mArrayPos[i]==-1){
				nBlankPos = i;
				break;
			}
		}
		return nBlankPos;
	}
	
	public void touchAt(float pixelx, float pixely){
		int x = (int) (pixelx/(this.getWidth()/mLevel));
		int y = (int) (pixely/(this.getHeight()/mLevel));
		int nBlankPos = this.getBlankPos();
		int nPos = y*mLevel+x;
		if(nPos==nBlankPos) return;
		//check is valid pos for switch
		if(Math.abs(nPos-nBlankPos)!=1 && Math.abs(nBlankPos-nPos)!=mLevel){		
			return;
		}else{
			Log.i("info--------", "swith "+nPos+"and "+nBlankPos);
			mArrayPos[nBlankPos]=mArrayPos[nPos];
			mArrayPos[nPos]=-1;			
			this.invalidate();
		}
		if(isGameOver()){			
			AlertDialog dlg =  new AlertDialog.Builder(this.getContext()).setTitle("确认")
		 	.setMessage("游戏完成, 是否再来一次？")
		 	.setPositiveButton("是", new DialogInterface.OnClickListener() {				
				public void onClick(DialogInterface dialog, int which) {
					// TODO Auto-generated method stub
					GameView.this.mStatus = GAME_STATUS.PLAYING;
					disorderBlocks();
					GameView.this.invalidate();
				}
			})
		 	.setNegativeButton("否", new DialogInterface.OnClickListener() {
				
				@Override
				public void onClick(DialogInterface dialog, int which) {
					// TODO Auto-generated method stub
					//System.exit(0);
					GameView.this.mStatus = GAME_STATUS.STATE_PREVIEW;
					invalidate();
				}
			})
		 	.show();
			
		}
	}
	public GAME_STATUS GetStatus() {return mStatus;}
	public int GetLevel()  { return mLevel;}
	//set image from draw
	private Bitmap mBmp=null;//image for display
	private int []mArrayPos=null;
	private int mLevel=3;	//游戏等级
	private GAME_STATUS mStatus;
	
}
