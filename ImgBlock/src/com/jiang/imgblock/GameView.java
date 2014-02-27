package com.jiang.imgblock;

import com.example.imgblock.R;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Point;
import android.graphics.Rect;
import android.graphics.drawable.BitmapDrawable;
import android.view.View;

public class GameView extends View {


	public GameView(Context context) {
		super(context);
		this.setImage(R.drawable.img0);
		this.setLevel(3);
	}

	@Override
	protected void onDraw(Canvas canvas) {
		
		Paint paint = new Paint();
		paint.setColor(Color.BLUE);
		canvas.drawRect(new Rect(0, 100, 299,300), paint);
		//draw bitmap...
		if(this.mBmp != null){
			Bitmap bmp = this.mBmp.getBitmap();
			for(int i=0; i<arrayPos.length; i++)
			{
				int x, y;
				int nSrcPos = arrayPos[i];
				x = nSrcPos%mLevel;
				y = nSrcPos/mLevel;
				Rect src = new Rect(x*bmp.getWidth()/mLevel, y*bmp.getHeight()/mLevel, 
						(x+1)*bmp.getWidth()/mLevel, (y+1)*bmp.getHeight()/mLevel);
				
				int nDstPos = i;
				x = nDstPos%mLevel;
				y = nSrcPos/mLevel;
				Rect dst = new Rect(x*canvas.getWidth()/mLevel, y*canvas.getHeight()/mLevel, 
						(x+1)*canvas.getWidth()/mLevel, (y+1)*canvas.getHeight()/mLevel);
				canvas.drawBitmap(this.mBmp.getBitmap(), src, dst, paint);				
			}
			paint.setColor(Color.RED);
			//draw grid
			for(int i=0; i<this.mLevel; i++)
				canvas.drawLine(canvas.getWidth()*i/mLevel, 0, canvas.getWidth()*i/mLevel, canvas.getHeight(), paint);
			for(int i=0; i<this.mLevel; i++)
				canvas.drawLine(0, canvas.getHeight()*i/mLevel, canvas.getWidth(), canvas.getHeight()*i/mLevel, paint);
							
		}
		super.onDraw(canvas);
	}
	
	public void setImage(int id){
		this.mBmp = (BitmapDrawable)getResources().getDrawable(id);
		this.postInvalidate();
	}
	//set game level
	public void setLevel(int nLevel){
		if(nLevel<3 || nLevel>6) return;
		this.arrayPos = new int[nLevel*nLevel];
		this.mLevel = nLevel;
		for(int i=0; i<nLevel*nLevel; i++)
			this.arrayPos[i]=i;
	}
	
	public void touchAt(Point pt){
		int x = pt.x/(this.getWidth()/mLevel);
		int y = pt.y/(this.getHeight()/mLevel);
		
		for(int i=0; i<arraryPos.length; i++)
			if(arr)
		
	}	
	//set image from draw
	private BitmapDrawable mBmp=null;//image for display
	private int []arrayPos=null;
	private int mLevel=3;
	
	
}
